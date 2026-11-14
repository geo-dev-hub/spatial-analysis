"""Dense local Lucas–Kanade optical flow for two regular image frames."""
from __future__ import annotations
import numpy as np
from scipy.ndimage import uniform_filter

def lucas_kanade(first,second,window_size=9,min_determinant=1e-6):
    """Estimate dense local flow (u=column/x, v=row/y) between two frames.

    Spatial gradients are averaged across frames; temporal gradient is
    second-first. Local normal equations are averaged over a square window.
    Pixels with insufficient two-direction texture are marked invalid and
    receive NaN flow. This is a single-scale small-motion teaching baseline.
    """
    a=np.asarray(first,dtype=float);b=np.asarray(second,dtype=float)
    if a.ndim!=2 or a.shape!=b.shape or min(a.shape)<2:raise ValueError("frames must be equally shaped 2D arrays")
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):raise ValueError("frames must be finite")
    if not isinstance(window_size,int) or isinstance(window_size,bool) or window_size<1 or window_size%2==0:raise ValueError("window_size must be a positive odd integer")
    if not np.isfinite(min_determinant) or min_determinant<0:raise ValueError("min_determinant must be finite and non-negative")
    gy,gx=np.gradient((a+b)/2.0);gt=b-a
    avg=lambda z:uniform_filter(z,size=window_size,mode="reflect")
    xx=avg(gx*gx);xy=avg(gx*gy);yy=avg(gy*gy)
    xt=avg(gx*gt);yt=avg(gy*gt)
    det=xx*yy-xy*xy
    valid=det>min_determinant
    u=np.full(a.shape,np.nan);v=np.full(a.shape,np.nan)
    u[valid]=(-yy[valid]*xt[valid]+xy[valid]*yt[valid])/det[valid]
    v[valid]=(xy[valid]*xt[valid]-xx[valid]*yt[valid])/det[valid]
    return {"u":u,"v":v,"valid":valid,"determinant":det}
