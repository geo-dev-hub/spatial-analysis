# Curves and smoothing: choose interpolation, approximation or filtering

A sequence of measured coordinates is not automatically a smooth curve. Before selecting a method, decide what the points mean: must the curve pass through every observation, approximate a control shape, preserve exact design geometry, or estimate a hidden trajectory from noisy measurements? These are different objectives.

This lesson introduces Chaikin corner cutting, Catmull–Rom interpolation, Bézier curves, B-splines, NURBS and state-space smoothing. It does not treat them as interchangeable curve generators.

## 1. Four different problems

| Problem | Desired behaviour | Candidate family |
|---|---|---|
| Draw a designed shape from handles | Curve is controlled by a small set of control points | Bézier |
| Smooth a control polygon | Curve approximates rather than passes through every vertex | Chaikin / B-spline |
| Interpolate waypoints | Curve passes through specified data points | Catmull–Rom or fitted spline |
| Estimate a latent path from noisy observations | Balance observations with a motion/process model | Kalman filter and smoother |

For a measured road or river centreline, smoothing is not automatically a cartographic improvement. It may remove bends, move the path across barriers, or create shortcuts through buildings and water. Preserve the observations and record the transformation.

## 2. Chaikin corner cutting

For each consecutive pair Pᵢ and Pᵢ₊₁, standard Chaikin refinement inserts two points:

$$
Q_i=\tfrac34P_i+\tfrac14P_{i+1},\qquad
R_i=\tfrac14P_i+\tfrac34P_{i+1}.
$$

Repeating the process cuts off corners and approaches a uniform quadratic B-spline limit curve under the usual subdivision setup. The method is simple and local, but it does not interpolate the original interior vertices: the curve generally moves inside the control polygon.

Open and closed curves need different endpoint handling. A naive open-polyline implementation can shorten or shift endpoints at every iteration. If endpoints must be retained, pin them explicitly or use a boundary rule designed for that requirement.

**Use it for:** visual smoothing of control polygons when approximation is acceptable.

**Do not use it for:** a measured route that must pass through each observation, or where a fixed boundary must remain exact without an explicit endpoint policy.

## 3. Catmull–Rom: interpolate waypoints

Catmull–Rom splines are cubic interpolating splines. Each segment is defined from four consecutive points, and the segment between the middle pair passes through those two points. Tangents are estimated from neighbouring points.

Uniform parameterisation can produce loops or cusps when waypoint spacing varies greatly. Chordal and centripetal parameterisations use distance-dependent knot spacing; centripetal parameterisation is often a safer starting point for unevenly spaced waypoints, but it is not a universal guarantee against every application-specific failure.

A curve passing through all waypoints is not necessarily a valid road or river. Check self-intersections, corridor constraints, curvature, endpoint tangents and deviation from observations.

## 4. Bézier curves

A degree-n Bézier curve with control points P₀,…,Pₙ is

$$
B(t)=\sum_{i=0}^{n}\binom{n}{i}(1-t)^{n-i}t^iP_i,
\qquad 0\leq t\leq1.
$$

It interpolates the first and last control points, but generally not the interior control points. The curve lies in the convex hull of its control points. The de Casteljau algorithm evaluates it using repeated linear interpolation and is numerically useful for subdivision.

Bézier segments are easy to edit, but a high-degree curve can be difficult to control locally. Piecewise Bézier segments need continuity conditions at joins. Matching endpoint positions gives positional continuity; matching tangent directions gives geometric tangent continuity; matching derivatives gives parametric continuity.

## 5. B-splines and NURBS

A B-spline is a piecewise-polynomial curve defined by control points, degree and a nondecreasing knot vector. Its basis functions are local: changing one control point affects only a limited parameter interval. Knot multiplicity controls continuity at a knot.

A NURBS curve is a rational B-spline:

$$
C(u)=\frac{\sum_i N_{i,p}(u)w_iP_i}
{\sum_i N_{i,p}(u)w_i}.
$$

Here Nᵢ,ₚ are degree-p B-spline basis functions, Pᵢ are control points and wᵢ are weights. NURBS can represent conic sections exactly and are widely used in CAD and geometric design. The weights are not statistical confidence values.

B-splines and NURBS are strong choices when local control, smoothness and design geometry matter. They are not automatically the right model for a noisy GPS trajectory or a network constrained to a street graph.

## 6. Kalman filtering and Rauch–Tung–Striebel smoothing

Kalman methods solve a different problem. They estimate a hidden state that evolves over time and is observed with noise. A linear state-space model is

$$
x_k=F_kx_{k-1}+w_k,\
z_k=H_kx_k+v_k,
$$

where xₖ is the latent state, zₖ the observation, Fₖ the transition model, Hₖ the observation model, and wₖ and vₖ are process and observation noise with declared covariance matrices.

The forward Kalman filter estimates each state using observations available up to that time. A Rauch–Tung–Striebel (RTS) smoother runs backward through the filtered sequence and uses later observations to refine earlier state estimates. This is a batch/offline smoother, not a geometric spline.

A common constant-velocity state in a planar system is x=[positionₓ, positionᵧ, velocityₓ, velocityᵧ]ᵀ. For time step Δt, the transition matrix includes position updates by velocity. The process-noise model encodes how much acceleration or other motion variation is expected. Poorly chosen noise covariance can over-smooth genuine turns or follow measurement noise too closely.

Use a suitable projected coordinate system or a local tangent frame before applying Euclidean motion models to geographic coordinates. For road-constrained movement, map matching or a network-aware state model may be needed; unconstrained Kalman smoothing can move a trajectory off the road.

## 7. Choosing and validating a method

1. **Interpolation or approximation?** Record whether original points must lie on the output.
2. **Local or global control?** Prefer local-support bases when edits should not alter distant sections.
3. **Geometry or noisy time series?** Splines model shape; Kalman methods model a latent evolving state.
4. **Constraints?** Check topology, barriers, network membership, endpoints and minimum separation.
5. **Parameterisation?** Document uniform, chordal or centripetal choices and knot conventions.
6. **Error?** Measure deviation from the source, not only visual smoothness.
7. **Scale and purpose?** A display line, engineering alignment and scientific trajectory have different tolerances.

For geographic lines, compute distances in an appropriate projected CRS or geodesic framework. A smooth curve can overshoot between observations; sample it densely enough to detect loops and intersections, but remember that finite sampling cannot prove the continuous curve is topology-safe.

## 8. Reproducible test cases

Include straight and sharply turning paths; uneven waypoint spacing; repeated points; coincident consecutive points; open and closed curves; very short segments; large coordinate magnitudes; noisy constant-velocity motion; abrupt turns; missing observations; and paths near barriers.

Report input point count, output sampling interval, coordinate units, method and parameters, endpoint policy, maximum deviation, length change, self-intersection count and any network/corridor violations. Preserve original observations separately from derived geometry.

## Further reading

- Chaikin, G. M. (1974), “An Algorithm for High-Speed Curve Generation,” *Computer Graphics and Image Processing*. See the discussion of the method's relationship to quadratic B-splines in [de Boor (1987), “Cutting corners always works”](https://doi.org/10.1016/0167-8396(87)90029-X).
- [B-spline curves chapter](https://www.cs.cmu.edu/afs/cs/academic/class/15456-f15/Handouts/CAGD-chapter8.pdf), Carnegie Mellon University course material, including Chaikin corner cutting and knot insertion.
- [Catmull–Rom spline discussion](https://doi.org/10.1007/s42979-021-00770-x), including interpolating behaviour and segment construction.
- Rauch, H. E., Tung, F. and Striebel, C. T. (1965), “Maximum Likelihood Estimates of Linear Dynamic Systems,” *AIAA Journal*, 3(8), 1445–1450. [DOI record](https://doi.org/10.2514/3.3166).

## Scope

**Implemented teaching baseline:** [Chaikin corner cutting, centripetal/uniform/chordal Catmull–Rom interpolation and arbitrary-degree Bézier evaluation](../implementations/python/curves-smoothing/README.md), with [tests](../implementations/python/curves-smoothing/test_curves_smoothing.py), an [intern walkthrough](../implementations/python/curves-smoothing/implementation-walkthrough.md) and an [executable lab notebook](../notebooks/curves-smoothing-lab.ipynb). B-spline and NURBS evaluation/fitting, Schneider-style Bezier fitting, Kalman filtering and RTS smoothing remain unimplemented and require separate numerical contracts and validation.


## Reproducible spline evaluation

The companion Python package now evaluates polynomial B-splines and rational NURBS using de Boor's algorithm. It accepts planar control points, degree, a nondecreasing knot vector and a parameter in the closed spline domain. NURBS evaluation lifts weighted controls into homogeneous coordinates, applies the same de Boor recursion, then projects back to the plane. Tests include polynomial Bezier equivalence and an exact rational quadratic quarter-circle midpoint.

- [B-spline and NURBS implementation](../implementations/python/curves-smoothing/splines.py)
- [Tests](../implementations/python/curves-smoothing/test_splines.py)
- [Intern walkthrough](../implementations/python/curves-smoothing/implementation-walkthrough.md)
- [Spline lab notebook](../notebooks/bspline-nurbs-lab.ipynb)

This is evaluation, not curve fitting. Schneider's recursive cubic Bezier fitting is now implemented in a separate module; Kalman/RTS state estimation is a distinct model family described below.


## Reproducible Kalman filtering and RTS smoothing

A NumPy-based companion module now implements a general linear-Gaussian state model with a forward Kalman filter and backward Rauch–Tung–Striebel smoother. It supports vector states, scalar or vector observations, missing measurement components, covariance validation and Joseph-form covariance updates. The initial state/covariance are interpreted as the prior before the first transition. This is a bounded linear model; it is not an EKF/UKF, particle smoother or map matcher.

- [Kalman/RTS implementation](../implementations/python/curves-smoothing/kalman_smoothing.py)
- [Tests](../implementations/python/curves-smoothing/test_kalman_smoothing.py)
- [Intern walkthrough](../implementations/python/curves-smoothing/kalman-smoothing-walkthrough.md)
- [Synthetic trajectory lab](../notebooks/kalman-rts-smoothing-lab.ipynb)


## Schneider's automatic cubic fitting

The companion curve-fitting module implements Schneider's recursive piecewise-cubic algorithm: chord-length parameterisation, least-squares tangent handle lengths, bounded Newton–Raphson reparameterisation and recursive splitting at the maximum-error sample. Its tolerance is a maximum squared residual in coordinate units squared. The output is a chain of connected cubic Bezier segments; this is not polyline simplification and does not guarantee tangent continuity at split points.

- [Implementation](../implementations/python/curves-smoothing/curve_fitting.py)
- [Tests](../implementations/python/curves-smoothing/test_curve_fitting.py)
- [Walkthrough](../implementations/python/curves-smoothing/curve-fitting-walkthrough.md)
- [Executable fitting lab](../notebooks/schneider-bezier-fitting-lab.ipynb)
- Primary source: Schneider (1990), *Graphics Gems*, pp. 612–626; [original paper PDF](https://lhf.impa.br/cursos/tmg/Schneider-1990.pdf).
