# Geodetic, ECEF and local ENU coordinates

This package connects three coordinate frames:

- **Geodetic:** longitude, geodetic latitude and ellipsoidal height on a named reference ellipsoid.
- **ECEF:** Earth-Centred, Earth-Fixed Cartesian coordinates (X, Y, Z), in metres.
- **ENU:** a local East, North, Up Cartesian frame whose origin and orientation are fixed at a chosen geodetic point.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Example

```python
from ecef_enu import geodetic_to_enu

local = geodetic_to_enu(
    longitude_deg=[36.82, 36.83],
    latitude_deg=[-1.29, -1.28],
    ellipsoidal_height_m=[1700, 1705],
    origin_longitude_deg=36.82,
    origin_latitude_deg=-1.29,
    origin_ellipsoidal_height_m=1700,
)
print(local)  # columns are East, North, Up in metres
```

The default ellipsoid is WGS 84. The API uses longitude/latitude order explicitly and degrees for angular inputs. Heights are **ellipsoidal heights**, not orthometric heights above mean sea level. Converting a DEM height or a GNSS height requires checking its vertical datum and applying an appropriate geoid model when needed.

## Mathematical model

For geodetic latitude `φ`, longitude `λ`, ellipsoidal height `h`, semi-major axis `a` and first eccentricity squared `e²`, define the prime-vertical radius:

```
N(φ) = a / sqrt(1 - e² sin²φ)
```

Then:

```
X = (N + h) cosφ cosλ
Y = (N + h) cosφ sinλ
Z = (N(1 - e²) + h) sinφ
```

For an origin at geodetic longitude `λ₀` and latitude `φ₀`, subtract its ECEF position and rotate the difference:

```
[ E ]   [ -sinλ₀        cosλ₀       0 ] [ ΔX ]
[ N ] = [ -sinφ₀cosλ₀ -sinφ₀sinλ₀ cosφ₀ ] [ ΔY ]
[ U ]   [  cosφ₀cosλ₀  cosφ₀sinλ₀ sinφ₀ ] [ ΔZ ]
```

The rotation is orthonormal. Its transpose maps ENU differences back into ECEF. The local frame is tangent to the reference ellipsoid at the origin; it is not a global map projection.

## Validation

The tests reproduce the published EPSG:9836 geocentric-to-topocentric example to millimetre-level tolerance, check the geodetic-to-ECEF equator and pole cases, verify round trips and batch broadcasting, and reject invalid coordinates.

## Scope and limitations

This is a small numerical teaching implementation for a static local tangent frame. It does not transform between datums or coordinate reference frames, estimate a geoid, convert orthometric to ellipsoidal height, model tectonic plate motion, or account for epoch-dependent reference frames. It does not replace a fully specified PROJ pipeline for production geodetic workflows.

See the [method lesson](../../../algorithms/geodesy/ecef-enu.md) and [intern walkthrough](implementation-walkthrough.md).
