import numpy as np

def gneiting_covariance(spatial_distance, temporal_lag, *, variance=1.0, spatial_scale=1.0, temporal_scale=1.0, alpha=1.0, beta=1.0, spatial_dimension=2):
    """Gneiting-class covariance on Euclidean space crossed with linear time."""
    h=np.asarray(spatial_distance,dtype=float); u=np.asarray(temporal_lag,dtype=float)
    if not np.all(np.isfinite(h)) or np.any(h<0): raise ValueError("spatial distances must be finite and non-negative")
    if not np.all(np.isfinite(u)): raise ValueError("temporal lags must be finite")
    if not np.isfinite(variance) or variance<0: raise ValueError("variance must be non-negative")
    if not np.isfinite(spatial_scale) or spatial_scale<=0: raise ValueError("spatial_scale must be positive")
    if not np.isfinite(temporal_scale) or temporal_scale<=0: raise ValueError("temporal_scale must be positive")
    if not np.isfinite(alpha) or not 0<alpha<=1: raise ValueError("alpha must lie in (0, 1]")
    if not np.isfinite(beta) or not 0<=beta<=1: raise ValueError("beta must lie in [0, 1]")
    if isinstance(spatial_dimension,bool) or not isinstance(spatial_dimension,(int,np.integer)) or spatial_dimension<1: raise ValueError("spatial_dimension must be a positive integer")
    q=1+(np.abs(u)/temporal_scale)**(2*alpha)
    return variance*q**(-beta*spatial_dimension/2)*np.exp(-((h/spatial_scale)**2)/(q**beta))

def gneiting_covariance_matrix(coordinates,times,**kwargs):
    xy=np.asarray(coordinates,dtype=float); t=np.asarray(times,dtype=float)
    if xy.ndim!=2 or xy.shape[0]==0 or xy.shape[1]==0: raise ValueError("coordinates must be a non-empty (n,d) array")
    if t.ndim!=1 or len(t)!=len(xy): raise ValueError("times must match coordinate rows")
    if not np.all(np.isfinite(xy)) or not np.all(np.isfinite(t)): raise ValueError("coordinates and times must be finite")
    h=np.linalg.norm(xy[:,None,:]-xy[None,:,:],axis=-1); u=np.abs(t[:,None]-t[None,:])
    return gneiting_covariance(h,u,spatial_dimension=xy.shape[1],**kwargs)

def covariance_matrix_diagnostics(matrix,tolerance=1e-10):
    K=np.asarray(matrix,dtype=float)
    if K.ndim!=2 or K.shape[0]!=K.shape[1] or K.shape[0]==0: raise ValueError("matrix must be non-empty and square")
    if not np.all(np.isfinite(K)): raise ValueError("matrix must be finite")
    if not np.isfinite(tolerance) or tolerance<0: raise ValueError("tolerance must be non-negative")
    symmetric=bool(np.allclose(K,K.T,atol=tolerance,rtol=0))
    minimum=float(np.linalg.eigvalsh((K+K.T)/2)[0])
    return {"symmetric":symmetric,"minimum_eigenvalue":minimum,"positive_semidefinite":bool(symmetric and minimum>=-tolerance)}
