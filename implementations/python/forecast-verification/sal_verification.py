"""Structure-Amplitude-Location (SAL) precipitation verification baseline."""
from __future__ import annotations
import numpy as np
from scipy.ndimage import label


def _precipitation(values, name):
    a=np.asarray(values,dtype=float)
    if a.ndim!=2 or min(a.shape)<2 or not np.all(np.isfinite(a)) or np.any(a<0):
        raise ValueError(f"{name} must be a finite non-negative 2D field at least 2x2")
    return a


def _field_objects(field, threshold_fraction, connectivity):
    peak=float(field.max())
    if peak<=0: return []
    threshold=threshold_fraction*peak
    structure=np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=int) if connectivity==4 else np.ones((3,3),dtype=int)
    labels,count=label(field>=threshold,structure=structure)
    objects=[]
    for object_id in range(1,count+1):
        rows,cols=np.where(labels==object_id)
        values=field[rows,cols]
        mass=float(values.sum())
        if mass<=0: continue
        objects.append({"id":len(objects)+1,"area":int(rows.size),
                        "mass":mass,"maximum":float(values.max()),
                        "scaled_volume":mass/float(values.max()),
                        "centroid_x":float(np.sum(cols*values)/mass),
                        "centroid_y":float(np.sum(rows*values)/mass)})
    return objects


def _weighted_object_volume(objects):
    total=sum(obj["mass"] for obj in objects)
    if total<=0: return None
    return float(sum(obj["mass"]*obj["scaled_volume"] for obj in objects)/total)


def _object_scatter(objects, centre):
    total=sum(obj["mass"] for obj in objects)
    if total<=0: return None
    return float(sum(obj["mass"]*np.hypot(obj["centroid_x"]-centre[0],
                                         obj["centroid_y"]-centre[1])
                     for obj in objects)/total)


def sal_score(forecast, observation, *, threshold_fraction=1/15, connectivity=8):
    """Compute Wernli-style SAL components on identical regular-grid fields.

    Objects are independently thresholded at threshold_fraction times each
    field's own maximum and labelled by connected components. This explicit
    connected-component choice is a teaching approximation to the original
    coherent-object identification. L is L1 + L2; no object matching occurs.
    """
    f=_precipitation(forecast,"forecast")
    o=_precipitation(observation,"observation")
    if f.shape!=o.shape: raise ValueError("forecast and observation must share a grid shape")
    fraction=float(threshold_fraction)
    if not np.isfinite(fraction) or fraction<=0 or fraction>1:
        raise ValueError("threshold_fraction must lie in (0, 1]")
    if connectivity not in (4,8): raise ValueError("connectivity must be 4 or 8")
    fmean=float(f.mean()); omean=float(o.mean())
    denominator=0.5*(fmean+omean)
    amplitude=0.0 if denominator==0 else float((fmean-omean)/denominator)
    fobjects=_field_objects(f,fraction,connectivity)
    oobjects=_field_objects(o,fraction,connectivity)
    fmass=float(f.sum()); omass=float(o.sum())
    if fmass==0 and omass==0:
        structure=0.0; location=0.0; l1=0.0; l2=0.0
        fcentre=ocentre=None; fscatter=oscatter=None
    elif fmass==0 or omass==0:
        structure=None; location=None; l1=None; l2=None
        fcentre=ocentre=None; fscatter=oscatter=None
    else:
        fv=_weighted_object_volume(fobjects); ov=_weighted_object_volume(oobjects)
        structure=float((fv-ov)/(0.5*(fv+ov)))
        rows,cols=f.shape
        rr,cc=np.indices(f.shape,dtype=float)
        fcentre=(float(np.sum(cc*f)/fmass),float(np.sum(rr*f)/fmass))
        ocentre=(float(np.sum(cc*o)/omass),float(np.sum(rr*o)/omass))
        dmax=float(np.hypot(rows-1,cols-1))
        l1=float(np.hypot(fcentre[0]-ocentre[0],fcentre[1]-ocentre[1])/dmax)
        fscatter=_object_scatter(fobjects,fcentre)
        oscatter=_object_scatter(oobjects,ocentre)
        l2=float(2.0*abs(fscatter-oscatter)/dmax)
        location=l1+l2
    return {"structure":structure,"amplitude":amplitude,"location":location,
            "location_l1":l1,"location_l2":l2,
            "forecast_objects":fobjects,"observation_objects":oobjects,
            "forecast_centre_of_mass":fcentre,"observation_centre_of_mass":ocentre,
            "forecast_object_scatter":fscatter,"observation_object_scatter":oscatter,
            "threshold_fraction":fraction,"connectivity":connectivity}
