"""Linear-Gaussian Kalman filtering and Rauch–Tung–Striebel smoothing."""
from __future__ import annotations
import numpy as np

def _matrix(value,name):
    a=np.asarray(value,dtype=float)
    if a.ndim!=2 or not np.all(np.isfinite(a)):raise ValueError(f"{name} must be a finite 2D matrix")
    return a

def _covariance(value,name,dimension):
    a=_matrix(value,name)
    if a.shape!=(dimension,dimension):raise ValueError(f"{name} has the wrong shape")
    if not np.allclose(a,a.T,atol=1e-10):raise ValueError(f"{name} must be symmetric")
    if np.linalg.eigvalsh(a).min() < -1e-9:raise ValueError(f"{name} must be positive semidefinite")
    return a

def kalman_rts_smoother(observations,transition,observation_matrix,process_covariance,
                        observation_covariance,initial_state,initial_covariance):
    """Filter then smooth a linear-Gaussian state-space sequence.

    observations has shape (time, observation_dimension); NaN entries denote
    missing observations. A fully missing row performs prediction only.
    Returns filtered and smoothed state means/covariances plus predictions.
    """
    F=_matrix(transition,"transition");H=_matrix(observation_matrix,"observation_matrix")
    x0=np.asarray(initial_state,dtype=float)
    if x0.ndim!=1 or not np.all(np.isfinite(x0)):raise ValueError("initial_state must be a finite vector")
    d=x0.size
    if F.shape!=(d,d) or H.ndim!=2 or H.shape[1]!=d:raise ValueError("transition/observation dimensions are inconsistent")
    m=H.shape[0]
    Q=_covariance(process_covariance,"process_covariance",d)
    R=_covariance(observation_covariance,"observation_covariance",m)
    P0=_covariance(initial_covariance,"initial_covariance",d)
    Y=np.asarray(observations,dtype=float)
    if Y.ndim==1 and m==1:Y=Y.reshape(-1,1)
    if Y.ndim!=2 or Y.shape[1]!=m or Y.shape[0]<1 or np.any(np.isinf(Y)):raise ValueError("observations must be a non-empty time-by-measurement array; NaN means missing")
    n=Y.shape[0]
    xf=np.zeros((n,d));Pf=np.zeros((n,d,d));xp=np.zeros((n,d));Pp=np.zeros((n,d,d))
    x=x0.copy();P=P0.copy();I=np.eye(d)
    for t in range(n):
        x=F@x;P=F@P@F.T+Q
        P=(P+P.T)/2;xp[t]=x;Pp[t]=P
        valid=np.isfinite(Y[t])
        if np.any(valid):
            Ht=H[valid,:];Rt=R[np.ix_(valid,valid)];yt=Y[t,valid]
            innovation=yt-Ht@x;S=Ht@P@Ht.T+Rt
            K=np.linalg.solve(S,(P@Ht.T).T).T
            x=x+K@innovation
            # Joseph form is more numerically stable than (I-KH)P.
            A=I-K@Ht;P=A@P@A.T+K@Rt@K.T
            P=(P+P.T)/2
        xf[t]=x;Pf[t]=P
    xs=xf.copy();Ps=Pf.copy()
    for t in range(n-2,-1,-1):
        J=np.linalg.solve(Pp[t+1],(Pf[t]@F.T).T).T
        xs[t]=xf[t]+J@(xs[t+1]-xp[t+1])
        Ps[t]=Pf[t]+J@(Ps[t+1]-Pp[t+1])@J.T
        Ps[t]=(Ps[t]+Ps[t].T)/2
    return {"predicted_means":xp,"predicted_covariances":Pp,
            "filtered_means":xf,"filtered_covariances":Pf,
            "smoothed_means":xs,"smoothed_covariances":Ps}
