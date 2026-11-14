# Geodetic coordinates, ECEF and the local ENU frame

A latitude and longitude describe a position on an ellipsoid. They are useful for locating places, but they are awkward coordinates for many local calculations. A small displacement east, north or up is much easier to reason about in metres.

The geodetic → ECEF → ENU pipeline connects the global reference frame to a local Cartesian frame.

## Three frames, three different jobs

- **Geodetic coordinates** describe longitude, geodetic latitude and ellipsoidal height on a reference ellipsoid.
- **ECEF coordinates** describe the same position as Earth-Centred, Earth-Fixed Cartesian coordinates ((X,Y,Z)), with origin at the Earth's centre and axes fixed to the Earth.
- **ENU coordinates** describe a local displacement as East, North and Up from a chosen origin.

The local ENU axes are tangent to the reference ellipsoid at the origin. Up is the ellipsoid normal, not necessarily the radial line from the Earth's centre.

```mermaid
flowchart LR
    A[Longitude, latitude, ellipsoidal height] --> B[Geodetic to ECEF]
    B --> C[Earth-centred XYZ]
    C --> D[Subtract origin and rotate]
    D --> E[Local East, North, Up]
    E --> F[Local engineering or analysis]
```

## Geodetic to ECEF

Let geodetic latitude be (phi), longitude be (lambda), ellipsoidal height be (h), semi-major axis be (a), and first eccentricity squared be (e^2).

The prime-vertical radius of curvature is:

[
N(phi)=rac{a}{sqrt{1-e^2sin^2phi}}.
]

Then:

[
egin{aligned}
X &= (N+h)cosphicoslambda,\
Y &= (N+h)cosphisinlambda,\
Z &= igl(N(1-e^2)+higr)sinphi.
end{aligned}
]

The ellipsoid matters. A spherical Earth approximation changes the result, especially away from the equator. The implementation uses WGS 84 by default and lets the learner specify another ellipsoid.

## ECEF to local ENU

Choose an origin with geodetic longitude (lambda_0), latitude (phi_0) and ellipsoidal height (h_0). Convert the origin to ECEF, then subtract it from each target point:

[
Deltamathbf{x}=
egin{bmatrix}
X-X_0\Y-Y_0\Z-Z_0
end{bmatrix}.
]

Rotate the difference into the local frame:

[
egin{bmatrix}E\N\Uend{bmatrix}
=
egin{bmatrix}
-sinlambda_0 & coslambda_0 & 0\
-sinphi_0coslambda_0 & -sinphi_0sinlambda_0 & cosphi_0\
cosphi_0coslambda_0 & cosphi_0sinlambda_0 & sinphi_0
end{bmatrix}
Deltamathbf{x}.
]

The rows of this matrix are the local East, North and Up unit vectors expressed in ECEF coordinates. It is an orthonormal rotation, so its inverse is its transpose. This makes the reverse ENU-to-ECEF transformation straightforward.

## Why the origin matters

ENU is not a global projection. Move the origin and the axes rotate. Over a small region, local east/north distances are intuitive and useful. Over a large region, the ellipsoid's curvature becomes important and one local tangent plane is no longer an appropriate global representation.

## Height is not just height

The formula requires **ellipsoidal height**. Many elevation datasets store orthometric height, often described as height above mean sea level. These are different vertical quantities, related through a geoid model. Do not pass an orthometric DEM value into this transformation as if it were ellipsoidal height without a vertical-datum conversion.

## A published numerical check

The EPSG:9836 geocentric-to-topocentric example uses a WGS 84 topocentric origin at longitude (5^circ), latitude (55^circ), height (200) m, and an ECEF target of:

[
(3771793.968,;140253.342,;5124304.349) mathrm{m}.
]

The expected local coordinates are approximately:

[
(E,N,U)=(-189013.869,;-128642.040,;-4220.171) mathrm{m}.
]

The package tests reproduce this published example. It is an independent check on axis order, signs and the rotation matrix.

## When this is useful

- GNSS and surveying calculations;
- local sensor and asset positioning;
- robotics and navigation;
- engineering models around a fixed site;
- local distance and direction calculations before applying a network or physical model.

## Implementation and learning material

The [tested Python package](../../implementations/python/ecef-enu/README.md) includes geodetic-to-ECEF, ECEF-to-ENU, ENU-to-ECEF and a direct geodetic-to-ENU helper. The [intern walkthrough](../../implementations/python/ecef-enu/implementation-walkthrough.md) explains each calculation, while the [visual lab](../../notebooks/ecef-enu-lab.ipynb) lets you inspect the local frame.

## Scope and limitations

This is a static local-frame transformation. It does not perform datum transformations, geoid conversion, epoch propagation, plate-motion modelling or GNSS adjustment. A production workflow must identify the complete horizontal and vertical reference systems, coordinate epoch and transformation pipeline.

## References

- IOGP, *Geomatics Guidance Note 7, Part 2: Coordinate Conversions and Transformations including Formulas*, EPSG method 9836 and 9837.
- [PROJ documentation: Geocentric to topocentric conversion](https://proj.org/en/stable/operations/conversions/topocentric.html).
- [EPSG method 9836: Geocentric/topocentric conversions](https://epsg.io/9836-method).
- [ESA Navipedia: Transformations between ECEF and ENU coordinates](https://gssc.esa.int/navipedia/index.php/Transformations_between_ECEF_and_ENU_coordinates).
- [PROJ documentation: Geodetic to geocentric conversion](https://proj.org/en/stable/operations/conversions/cart.html).
