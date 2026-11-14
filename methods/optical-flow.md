# Optical flow for image sequences: Lucas–Kanade, Farnebäck and DIS

Optical flow estimates apparent motion between consecutive images. The output is a displacement vector field: for each pixel or feature, it estimates where the corresponding image content moved between frames.

In Earth observation, optical flow can support cloud-motion estimation, image registration, feature tracking, surface-change analysis and short-term advection nowcasting. It does not automatically measure physical object motion: the result depends on image formation, viewing geometry, temporal spacing and the assumptions of the algorithm.

## 1. The brightness-constancy model

Let I(x,y,t) be image intensity. A common starting assumption is that the intensity of a moving image point remains approximately constant:

$$
I(x,y,t)=I(x+u\Delta t,y+v\Delta t,t+\Delta t).
$$

For small displacements, a first-order Taylor expansion gives the optical-flow constraint:

$$
I_xu+I_yv+I_t=0,
$$

where u and v are horizontal and vertical image velocities and Iₓ, Iᵧ and Iₜ are spatial and temporal intensity derivatives.

This is one equation with two unknowns. A single pixel cannot determine both motion components. Algorithms introduce additional information through local constancy, spatial regularisation, patch matching or multi-scale refinement.

## 2. Lucas–Kanade: local patch motion

Lucas–Kanade assumes approximately constant motion within a small neighbourhood. For each pixel in the patch, the optical-flow constraint gives a linear equation. Stacking the equations yields

$$
A\begin{bmatrix}u\\v\end{bmatrix}=b,
$$

where each row of A contains image gradients and b contains negative temporal derivatives. A least-squares estimate is

$$
\begin{bmatrix}u\\v\end{bmatrix}
=(A^TA)^{-1}A^Tb,
$$

when the matrix is sufficiently well-conditioned.

The eigenvalues of AᵀA indicate whether the patch contains enough gradient information to constrain both motion components. A flat patch has little information; a straight edge constrains motion mainly perpendicular to the edge (the aperture problem). Corners and textured patches are more informative.

Lucas–Kanade is commonly used as a sparse feature-tracking method. Pyramidal variants extend the range of motion by estimating displacement at coarse resolution and refining it at finer levels.

**Strength:** efficient local tracking and a clear least-squares interpretation.

**Limitations:** local constant-motion assumption, dependence on texture, sensitivity to large motion without pyramids, and track loss under occlusion or appearance change.

## 3. Farnebäck: dense motion from polynomial expansion

Farnebäck approximates local image neighbourhoods with quadratic polynomials. It estimates how the polynomial coefficients change under translation and uses that relationship to infer displacement. Refinement across scales produces a dense flow field.

Compared with sparse Lucas–Kanade tracking, Farnebäck estimates motion for a dense set of pixels. It is useful when a complete displacement field is needed, but the result can be less reliable in textureless regions, occlusions and areas with strong radiometric changes.

Implementation parameters such as pyramid scale, number of levels, window size, iterations and polynomial neighbourhood affect the accuracy/runtime trade-off. Record them with the result.

## 4. DIS: Dense Inverse Search

Dense Inverse Search (DIS) was designed to balance dense-flow accuracy and computational efficiency. The method combines inverse search for patch correspondences, multi-scale aggregation to create a dense displacement field, and variational refinement.

The OpenCV implementation exposes presets for different speed/quality trade-offs and adds options such as spatial propagation and initial-flow input. Those are implementation details; a package should record the library version and preset rather than treating all DIS outputs as identical.

**Strength:** fast dense flow for practical image-sequence processing.

**Limitations:** still depends on image correspondence and can fail under occlusion, large appearance changes, weak texture or motion outside its search/refinement range.

## 5. Compare the families

| Method | Output | Core assumption/strategy | Good fit |
|---|---|---|---|
| Lucas–Kanade | Usually sparse tracks; dense variants exist | Local constant motion, gradient least squares | Feature tracking and local displacement |
| Farnebäck | Dense flow | Polynomial expansion and multi-scale refinement | Dense displacement between image pairs |
| DIS | Dense flow | Patch inverse search, aggregation and refinement | Fast dense flow with tunable speed/quality |

These methods estimate apparent image motion. They are not interchangeable with geodesic paths, physical wind fields, object tracking or image registration, although their outputs may be inputs to those workflows.

## 6. Convert image displacement to map displacement

Optical flow is usually expressed in pixel coordinates. For a georeferenced raster with affine transform

$$
\begin{bmatrix}X\\Y\end{bmatrix}
=
\begin{bmatrix}a&b\\d&e\end{bmatrix}
\begin{bmatrix}c\\r\end{bmatrix}
+
\begin{bmatrix}x_0\\y_0\end{bmatrix},
$$

a pixel displacement (u,v) corresponds to map-coordinate displacement

$$
\begin{bmatrix}\Delta X\\\Delta Y\end{bmatrix}
=
\begin{bmatrix}a&b\\d&e\end{bmatrix}
\begin{bmatrix}u\\v\end{bmatrix}.
$$

This conversion is essential for rotated or sheared rasters. For north-up grids, row direction commonly increases southward, so the sign of the northing displacement must be handled correctly.

Map displacement is still not necessarily ground motion. If the sensor, platform, view angle, terrain relief or orthorectification changes between images, apparent displacement can include parallax and registration error. Convert to physical velocity only after accounting for acquisition-time interval and image geometry.

## 7. Earth-observation failure modes

- **Radiometric change:** brightness constancy may fail between sensors, seasons, illumination conditions or atmospheric states.
- **Clouds and shadows:** moving cloud shadows can be mistaken for surface motion.
- **Occlusion and disocclusion:** a pixel may have no valid correspondence in the next image.
- **Geometric misregistration:** residual co-registration error appears as a coherent flow field.
- **Terrain parallax:** off-nadir views over elevated terrain can create apparent displacement.
- **Temporal gap:** long intervals allow large changes and violate small-motion assumptions.
- **Textureless areas:** flow is poorly constrained; report confidence or validity masks.
- **Moving boundaries:** water, snow, vegetation and cloud edges may change shape rather than translate.
- **Image resampling:** differing grids and interpolation can alter local gradients and flow estimates.

Use quality masks and confidence diagnostics. A smooth-looking flow field is not proof of correct motion.

## 8. Validation

Use synthetic image pairs with known translations, rotations, scale changes, nonrigid deformations and occlusions. Measure endpoint error:

$$
EPE=\frac{1}{N}\sum_{i=1}^{N}
\sqrt{(u_i-\hat u_i)^2+(v_i-\hat v_i)^2},
$$

where (uᵢ,vᵢ) is reference flow and (ûᵢ, v̂ᵢ) is estimated flow.

Also report angular error, valid-pixel coverage, runtime, memory, and error stratified by texture, motion magnitude, occlusion and image region. For satellite sequences, compare against independent tie points or known motion where available. Do not evaluate on the same pairs used to tune parameters.

For advection nowcasting, evaluate the downstream forecast, not only optical-flow endpoint error. A flow field can have low pixel error but still produce poor rainfall forecasts if the transported field or growth/decay model is wrong.

## Further reading

- Lucas, B. D. and Kanade, T. (1981), “An Iterative Image Registration Technique with an Application to Stereo Vision,” *Proceedings of the Seventh International Joint Conference on Artificial Intelligence*, 674–679. [IJCAI proceedings record](https://ijcai.org/proceedings/1981/127).
- Farnebäck, G. (2003), “Two-Frame Motion Estimation Based on Polynomial Expansion,” *Scandinavian Conference on Image Analysis*, 363–370. [Author-hosted paper](https://www.ida.liu.se/ext/WITAS-ev/Computer_Vision_Technologies/Papers/scia03_farneback.pdf).
- Kroeger, T., Timofte, R., Dai, D. and Van Gool, L. (2016), “Fast Optical Flow using Dense Inverse Search,” *European Conference on Computer Vision*, 471–488. [DOI 10.1007/978-3-319-46493-0_29](https://doi.org/10.1007/978-3-319-46493-0_29).
- [OpenCV optical-flow documentation](https://docs.opencv.org/5.0/main_modules/video_track.html) and [DISOpticalFlow reference](https://docs.opencv.org/5.0/main_modules/classcv_1_1DISOpticalFlow.html) document implementation parameters and presets.

## Scope

This guide is paired with a tested teaching package: [Lucas–Kanade, Farnebäck and DIS implementations](../implementations/python/optical-flow/README.md), [Lucas–Kanade source](../implementations/python/optical-flow/lucas_kanade.py), [Farnebäck/DIS wrappers](../implementations/python/optical-flow/dense_optical_flow.py) and synthetic translation tests. Farnebäck and DIS call OpenCV; they are not reimplementations of the underlying papers. The package currently provides translation fixtures rather than a full benchmark. It distinguishes sparse/local tracking from dense-flow methods and explains conversion from pixel motion to map displacement. A future implementation should include synthetic ground-truth sequences, validity masks and georeferencing tests before applying the method to Earth-observation time series.


## Executable Lucas–Kanade baseline

The companion package implements a single-scale dense local Lucas–Kanade estimator for small motion. It forms local normal equations from spatial and temporal image gradients and marks low-texture windows invalid rather than returning unstable flow. A synthetic subpixel translation lab and tests are included. This does not implement Farnebäck, DIS or variational optical flow.

- [Implementation](../implementations/python/optical-flow/lucas_kanade.py)
- [Tests](../implementations/python/optical-flow/test_lucas_kanade.py)
- [Walkthrough](../implementations/python/optical-flow/implementation-walkthrough.md)
- [Lab](../notebooks/lucas-kanade-optical-flow-lab.ipynb)
