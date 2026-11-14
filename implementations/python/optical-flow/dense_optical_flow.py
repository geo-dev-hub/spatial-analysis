"""OpenCV-backed dense optical-flow teaching wrappers."""
from __future__ import annotations
import numpy as np

def _frames(first, second):
    a=np.asarray(first); b=np.asarray(second)
    if a.ndim != 2 or b.shape != a.shape or min(a.shape) < 8:
        raise ValueError("frames must be equally shaped 2D grayscale arrays at least 8x8")
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
        raise ValueError("frames must contain only finite values")
    if a.dtype != np.uint8:
        a=np.clip(a,0,255).astype(np.uint8)
    if b.dtype != np.uint8:
        b=np.clip(b,0,255).astype(np.uint8)
    return np.ascontiguousarray(a), np.ascontiguousarray(b)

def farneback(first, second, *, pyr_scale=0.5, levels=3, winsize=15,
              iterations=3, poly_n=5, poly_sigma=1.2, flags=0):
    """Dense Farnebäck flow; u is column displacement and v is row displacement."""
    import cv2
    a,b=_frames(first,second)
    if not 0 < float(pyr_scale) < 1: raise ValueError("pyr_scale must be in (0,1)")
    if not isinstance(levels,int) or levels < 1: raise ValueError("levels must be a positive integer")
    if not isinstance(winsize,int) or winsize < 3 or winsize % 2 == 0: raise ValueError("winsize must be odd and >=3")
    if not isinstance(iterations,int) or iterations < 1: raise ValueError("iterations must be positive")
    if poly_n not in (5,7): raise ValueError("poly_n must be 5 or 7")
    if not np.isfinite(poly_sigma) or poly_sigma <= 0: raise ValueError("poly_sigma must be positive")
    flow=cv2.calcOpticalFlowFarneback(a,b,None,float(pyr_scale),levels,winsize,
                                      iterations,poly_n,float(poly_sigma),int(flags))
    return {"u":flow[...,0],"v":flow[...,1],"valid":np.isfinite(flow).all(axis=2),
            "flow":flow,"method":"farneback","parameters":{
                "pyr_scale":float(pyr_scale),"levels":levels,"winsize":winsize,
                "iterations":iterations,"poly_n":poly_n,"poly_sigma":float(poly_sigma),
                "flags":int(flags)}}

def dis(first, second, *, preset="medium", finest_scale=0, patch_size=8,
        patch_stride=4, gradient_descent_iterations=25, variational_refinement=True):
    """Dense Inverse Search flow using OpenCV's DIS implementation."""
    import cv2
    a,b=_frames(first,second)
    presets={"ultrafast":cv2.DISOPTICAL_FLOW_PRESET_ULTRAFAST,
             "fast":cv2.DISOPTICAL_FLOW_PRESET_FAST,
             "medium":cv2.DISOPTICAL_FLOW_PRESET_MEDIUM}
    if preset not in presets: raise ValueError("preset must be ultrafast, fast or medium")
    if not isinstance(finest_scale,int) or finest_scale < 0: raise ValueError("finest_scale must be non-negative")
    if not isinstance(patch_size,int) or patch_size < 2: raise ValueError("patch_size must be >=2")
    if not isinstance(patch_stride,int) or patch_stride < 1: raise ValueError("patch_stride must be positive")
    if not isinstance(grad_descent_iterations,int) or grad_descent_iterations < 1:
        raise ValueError("grad_descent_iterations must be positive")
    algorithm=cv2.DISOpticalFlow_create(presets[preset])
    algorithm.setFinestScale(finest_scale)
    algorithm.setPatchSize(patch_size)
    algorithm.setPatchStride(patch_stride)
    algorithm.setGradientDescentIterations(grad_descent_iterations)
    algorithm.setVariationalRefinementIterations(5 if variational_refinement else 0)
    flow=algorithm.calc(a,b,None)
    return {"u":flow[...,0],"v":flow[...,1],"valid":np.isfinite(flow).all(axis=2),
            "flow":flow,"method":"dis","parameters":{
                "preset":preset,"finest_scale":finest_scale,"patch_size":patch_size,
                "patch_stride":patch_stride,"gradient_descent_iterations":grad_descent_iterations,
                "variational_refinement":bool(variational_refinement)}}
