"""Bounded methane-plume detection and emission-rate estimators.

These are transparent algorithmic baselines, not retrievals from radiance or
validated operational satellite products. Inputs are already converted to
physical enhancement/concentration fields.
"""
from __future__ import annotations
import numpy as np
from scipy.signal import correlate2d


def _finite_array(values, name, ndim=2):
    a=np.asarray(values,dtype=float)
    if a.ndim!=ndim or not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be a finite {ndim}D array")
    return a


def gaussian_plume_template(shape, sigma_cross, sigma_along, angle_radians=0.0):
    """Create a unit-peak rotated anisotropic Gaussian template."""
    if len(shape)!=2 or any(not isinstance(n,(int,np.integer)) or n<3 for n in shape):
        raise ValueError("shape must contain two integer dimensions >= 3")
    sx,sy=float(sigma_cross),float(sigma_along)
    angle=float(angle_radians)
    if not np.isfinite(sx) or not np.isfinite(sy) or sx<=0 or sy<=0 or not np.isfinite(angle):
        raise ValueError("sigmas must be positive finite values and angle finite")
    rows,cols=np.indices(shape,dtype=float)
    x=cols-(shape[1]-1)/2
    y=rows-(shape[0]-1)/2
    # Rotate coordinates so sigma_along follows the angle from +x.
    along=x*np.cos(angle)+y*np.sin(angle)
    cross=-x*np.sin(angle)+y*np.cos(angle)
    return np.exp(-0.5*((along/sy)**2+(cross/sx)**2))


def matched_filter_plume(image, templates, noise_sigma, *, threshold=3.0):
    """Scan one or more templates and return strongest standardized response.

    For each template t, amplitude is <image,t>/<t,t> and score is
    <image,t>/(noise_sigma*sqrt(<t,t>)); valid-only correlations avoid
    padding-induced edge detections. The maximum score over templates is kept.
    This assumes approximately white, zero-mean Gaussian residual noise.
    """
    data=_finite_array(image,"image")
    sigma=float(noise_sigma); cutoff=float(threshold)
    if not np.isfinite(sigma) or sigma<=0 or not np.isfinite(cutoff):
        raise ValueError("noise_sigma must be positive and threshold finite")
    if not templates:
        raise ValueError("at least one template is required")
    best_score=np.full(data.shape,-np.inf)
    best_amplitude=np.full(data.shape,np.nan)
    best_template=np.full(data.shape,-1,dtype=int)
    for ti,template in enumerate(templates):
        t=_finite_array(template,"template")
        if any(n%2==0 for n in t.shape) or any(n>m for n,m in zip(t.shape,data.shape)):
            raise ValueError("templates must have odd dimensions no larger than image")
        energy=float(np.sum(t*t))
        if energy<=0:
            raise ValueError("template must have non-zero energy")
        numerator=correlate2d(data,t,mode="same",boundary="fill",fillvalue=0)
        score=numerator/(sigma*np.sqrt(energy))
        amp=numerator/energy
        mask=score>best_score
        best_score[mask]=score[mask]
        best_amplitude[mask]=amp[mask]
        best_template[mask]=ti
    detections=best_score>=cutoff
    return {"score":best_score,"amplitude":best_amplitude,
            "template_index":best_template,"detections":detections}


def ime_emission_rate(ime_kg, wind_speed_m_s, characteristic_length_m):
    """Estimate Q = IME * wind speed / characteristic plume length (kg/s)."""
    ime=float(ime_kg);wind=float(wind_speed_m_s);length=float(characteristic_length_m)
    if not all(np.isfinite(v) for v in (ime,wind,length)) or ime<0 or wind<0 or length<=0:
        raise ValueError("IME and wind speed must be non-negative; length must be positive")
    return ime*wind/length


def cross_sectional_flux(concentration_kg_m3, normal_wind_m_s, segment_width_m):
    """Integrate concentration * normal wind * segment width (kg/s).

    Arrays describe samples along one plume cross-section. Signed normal wind
    is retained so reversed flow reverses the flux sign.
    """
    c=np.asarray(concentration_kg_m3,dtype=float)
    u=np.asarray(normal_wind_m_s,dtype=float)
    w=np.asarray(segment_width_m,dtype=float)
    if c.ndim!=1 or c.size==0 or u.shape!=c.shape or w.shape!=c.shape:
        raise ValueError("concentration, wind and width must be matching non-empty 1D arrays")
    if not all(np.all(np.isfinite(a)) for a in (c,u,w)) or np.any(c<0) or np.any(w<=0):
        raise ValueError("concentration must be non-negative, widths positive and all values finite")
    return float(np.sum(c*u*w))
