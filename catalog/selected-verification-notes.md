# Selected source-verification notes

Last updated: 14 November 2026

These notes record bounded checks against publisher or institutional bibliographic records. They do not mark an entire grouped source entry as verified. The dimensions remain separate under the [verification protocol](verification-protocol.md).

## Section 10 — Visvalingam–Whyatt line simplification

**Source entry:** “Line simplification variants: Reumann-Witkam, Lang, Opheim, Zhao-Saalfeld, Visvalingam-Whyatt with effective area” (source page 21).

- **Identity:** confirmed for the Visvalingam–Whyatt method named in the group.
- **Bibliography:** confirmed: Visvalingam, M. and Whyatt, J. D. (1993), “Line generalisation by repeated elimination of points,” *The Cartographic Journal*, 30(1), 46–51, DOI [10.1179/000870493786962263](https://doi.org/10.1179/000870493786962263).
- **Evidence:** Lancaster University's institutional research record and the Hull repository record both identify the article, journal, volume, issue, pages and DOI.
- **Technical claims:** the canonical lesson describes effective-area elimination and its distinction from Douglas–Peucker. This note verifies citation identity and metadata, not every implementation detail or every claim in the original paper.
- **Implementation:** the linked Python package is a tested open-polyline teaching baseline for Douglas–Peucker and Visvalingam–Whyatt; it does not cover Reumann–Witkam, Lang, Opheim or Zhao–Saalfeld.
- **Rights:** link to the DOI/institutional records; no paper text, figure or publisher PDF is reproduced here.
- **Remaining work:** split the grouped source row into child entries and review each named simplification variant independently.

## Section 10 — Spatial cross-validation and nearest-neighbour distance matching

**Source entry:** “Spatial cross-validation, NNDM, kNNDM, buffered leave-one-out, spatial k-fold by clustering, blockCV, spatial+temporal leave-out” (source page 21).

- **Identity:** confirmed for the NNDM and kNNDM methods discussed below; the grouped source entry still contains other designs and software names that require separate review.
- **Bibliography — NNDM:** confirmed: Milà, C., Mateu, J., Pebesma, E. and Meyer, H. (2022), “Nearest neighbour distance matching Leave-One-Out Cross-Validation for map validation,” *Methods in Ecology and Evolution*, 13(6), 1304–1316, DOI [10.1111/2041-210X.13851](https://doi.org/10.1111/2041-210X.13851). Publisher record confirms title, authors, date, journal issue and pages.
- **Bibliography — kNNDM:** confirmed: Linnenbrink, J., Milà, C., Ludwig, M. and Meyer, H. (2024), “kNNDM CV: k-fold nearest-neighbour distance matching cross-validation for map accuracy estimation,” *Geoscientific Model Development*, 17, 5897–5912, DOI [10.5194/gmd-17-5897-2024](https://doi.org/10.5194/gmd-17-5897-2024). The journal record confirms title, authors, date, volume, pages and DOI; the article is published under CC BY 4.0.
- **Technical claims checked:** the lesson's high-level distinction between prediction-oriented distance matching, spatial block CV and buffered LOO is grounded in the two primary papers. NNDM matches the distribution of nearest-neighbour distances from prediction to training locations with the corresponding test-to-training distribution. kNNDM seeks a k-fold configuration that approximates this distributional match. The papers' findings are scoped to their simulation and case-study settings; they do not establish universal superiority.
- **Important limitations:** nearest-neighbour distance matching uses geographical distances and does not by itself encode direction, anisotropy, nonstationarity or covariate-space shift. A probability-sample/design-based map-accuracy assessment remains preferable when feasible for the target population.
- **Implementation:** the existing Python package implements fixed planar grid blocks and optional buffered exclusion only. It does not implement NNDM or kNNDM. The lesson links to the maintained `blockCV` implementation as an external option; package versions and parameters must be recorded by users.
- **Rights:** link to publisher records; no article text or figures are reproduced.
- **Review date:** 14 November 2026.
- **Remaining work:** split the grouped source row into child entries and independently review spatial block CV, buffered LOO, NNDM, kNNDM, blockCV software, clustering-based folds and spatiotemporal holdouts.

## Section 22 — Nonseparable space-time covariance references

**Source entry:** “Space-time covariances: Gneiting nonseparable class, Cressie-Huang, product-sum and metric models” (source page 45).

### Cressie and Huang (1999)

- **Identity:** confirmed.
- **Bibliography:** confirmed: Cressie, N. and Huang, H.-C. (1999), “Classes of Nonseparable, Spatio-Temporal Stationary Covariance Functions,” *Journal of the American Statistical Association*, 94(448), 1330–1339, DOI [10.1080/01621459.1999.10473885](https://doi.org/10.1080/01621459.1999.10473885).
- **Evidence:** Taylor & Francis publisher record.
- **Technical claims:** not independently audited in this bibliography note.
- **Rights:** DOI link only; no article content is reproduced.

### Gneiting (2002)

- **Identity:** confirmed.
- **Bibliography:** confirmed: Gneiting, T. (2002), “Nonseparable, Stationary Covariance Functions for Space-Time Data,” *Journal of the American Statistical Association*, 97(458), 590–600, DOI [10.1198/016214502760047113](https://doi.org/10.1198/016214502760047113).
- **Evidence:** Taylor & Francis publisher record.
- **Technical claims:** the canonical lesson and package implement one Euclidean-space-by-linear-time member of a Gneiting class. The finite-matrix eigenvalue diagnostic is not a proof of positive definiteness for all samples or geometries. This note verifies citation metadata, not the complete mathematical conditions of the paper.
- **Rights:** DOI link only; no article content is reproduced.

**Scope warning:** the existing canonical record is not a comprehensive space-time covariance catalogue. Cressie–Huang, Gneiting, product-sum, metric, spherical and network covariance constructions are distinct families or settings. Only the stated Gneiting-class teaching member is implemented in the current package.

## Review metadata

- Review date: 14 November 2026.
- Review type: bibliographic identity and metadata check.
- Technical-claim status: not promoted by these notes.
- Rights status: link-only for the cited papers; no third-party content reused.


## Section 10 — Line clipping

**Source entry:** “Line clipping: Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, Nicholl-Lee-Nicholl” (source page 21).

- **Identity and technical scope:** the canonical lesson treats Cohen–Sutherland as an outcode/encoding method, Liang–Barsky as parametric clipping against an axis-aligned rectangle, and Cyrus–Beck as parametric clipping against convex half-spaces. It explicitly does not claim that Cyrus–Beck handles arbitrary concave windows or that segment clipping alone produces clipped polygon output.
- **Bibliography:** Matthes, J. and Drakopoulos, V. (2022), “Line Clipping in 2D: Overview, Techniques and Algorithms,” *Journal of Imaging*, 8(10), 286, DOI [10.3390/jimaging8100286](https://doi.org/10.3390/jimaging8100286). The publisher's open-access article surveys the major line-clipping families and named algorithms.
- **Technical-claim status:** the lesson's high-level taxonomy and algorithm distinctions are checked against the review. The equations are presented as teaching derivations; they have not been validated against a new implementation in this repository.
- **Implementation:** no new clipping implementation is claimed. The lesson includes a manual test plan but no executable test suite.
- **Rights:** DOI link only; no article text or figures reproduced.
- **Remaining work:** independently inspect the exact parameter-sign convention and edge cases in a future tested implementation; verify Nicholl–Lee–Nicholl separately if it becomes a full lesson.

## Section 10 — Rasterization and grid traversal

**Source entry:** “Line and polygon rasterization: Bresenham, DDA, Wu's anti-aliased line, scanline polygon fill, supercover lines” (source page 21).

- **Identity and scope:** the lesson distinguishes thin-line rasterisation, anti-aliased display, polygon scan conversion, supercover cell visitation and fractional-area coverage. It does not treat these outputs as interchangeable.
- **Bibliography:** Levoy, M., Stanford CS 248, [Rasterization algorithms](https://www.graphics.stanford.edu/courses/cs248-08/scan/scan1.html), lecture notes covering DDA, Bresenham and polygon scan conversion; Wu, X. (1991), “An Efficient Antialiasing Technique,” *Computer Graphics*, 25(4), 143–152, DOI [10.1145/127719.122734](https://doi.org/10.1145/127719.122734); Amanatides, J. and Woo, A. (1987), “A Fast Voxel Traversal Algorithm for Ray Tracing,” *Eurographics*, DOI [10.2312/egtp.19871000](https://doi.org/10.2312/egtp.19871000).
- **Technical-claim status:** method distinctions and the need to state sample, edge, corner and cell-coverage conventions are checked against the cited teaching and research sources. The lesson's cell-coverage equations are definitions, not claims that a particular library implements exact coverage.
- **Implementation:** no new rasterization or traversal code is claimed. The lesson includes a test-design specification.
- **Rights:** links only; no third-party text or figures reproduced.
- **Remaining work:** verify each algorithm's exact variant and build independent, tested implementations with explicit row/column, affine-grid, boundary and NoData contracts.


## Section 10 — Curves, subdivision and trajectory smoothing

**Source entry:** “Curves and smoothing: Chaikin corner cutting, Catmull-Rom, B-splines, NURBS, Bezier fitting (Schneider), Kalman and RTS smoothers” (source page 21).

- **Identity and scope:** the lesson separates approximating subdivision (Chaikin), interpolating splines (Catmull–Rom), parametric design curves (Bézier, B-spline and NURBS) and state estimation/smoothing (Kalman filter and Rauch–Tung–Striebel smoother). These are not equivalent operations.
- **Bibliography and evidence:** de Boor, C. (1987), “Cutting corners always works,” *Computer Aided Geometric Design*, 4(1–2), 125–131, DOI [10.1016/0167-8396(87)90029-X](https://doi.org/10.1016/0167-8396(87)90029-X), discusses convergence of corner-cutting schemes including Chaikin's algorithm. Carnegie Mellon University course notes provide a B-spline chapter describing knot insertion and Chaikin's relationship to uniform quadratic B-splines. A 2021 Springer paper discusses Catmull–Rom as a cubic interpolating spline. Rauch, Tung and Striebel (1965), “Maximum Likelihood Estimates of Linear Dynamic Systems,” *AIAA Journal*, 3(8), 1445–1450, DOI [10.2514/3.3166](https://doi.org/10.2514/3.3166), is the classical RTS smoother reference.
- **Technical-claim status:** the lesson distinguishes interpolation from approximation, rational spline weights from statistical weights, and offline RTS smoothing from geometric spline construction. It warns that unconstrained smoothing can violate road, river or barrier constraints. The lesson is a bounded overview, not a full mathematical treatment of every basis or filter variant.
- **Implementation:** no new spline or Kalman implementation is claimed.
- **Rights:** DOI and institutional links only; no source figures or text reproduced.
- **Remaining work:** verify the Schneider fitting method as its own algorithm; expand NURBS basis and knot multiplicity treatment; build separate spline and state-space implementations with numerical and geometry-specific tests.


## Section 10 — Geodesics on triangle meshes

**Source entry:** “Geodesics on meshes: MMP exact geodesics, Chen-Han, fast marching on triangle meshes” (source page 21).

- **Identity and bibliography — MMP:** Mitchell, J. S. B., Mount, D. M. and Papadimitriou, C. H. (1987), “The Discrete Geodesic Problem,” *SIAM Journal on Computing*, 16(4), 647–668, DOI [10.1137/0216045](https://doi.org/10.1137/0216045). The SIAM record confirms authors, venue, volume, issue, pages and the polyhedral shortest-path problem.
- **Identity and bibliography — Chen–Han:** Chen, J. and Han, Y. (1990), “Shortest Paths on a Polyhedron, Part I: Computing Shortest Paths,” *Proceedings of the Sixth Annual Symposium on Computational Geometry*, DOI [10.1145/98524.98601](https://doi.org/10.1145/98524.98601). The conference record and available paper identify the alternative exact algorithm for possibly nonconvex polyhedra.
- **Identity and bibliography — fast marching:** Kimmel, R. and Sethian, J. A. (1998), “Computing Geodesic Paths on Manifolds,” *Proceedings of the National Academy of Sciences*, 95(15), 8431–8435, DOI [10.1073/pnas.95.15.8431](https://doi.org/10.1073/pnas.95.15.8431). The paper extends fast marching to triangulated domains and uses it to compute geodesic distances and paths.
- **Technical-claim status:** the lesson distinguishes graph-edge shortest paths, exact polyhedral surface geodesics and numerical Eikonal/fast-marching solutions. Complexity claims are tied to the cited algorithm papers and are not attributed to arbitrary software implementations.
- **Implementation:** no new geodesic implementation is claimed. The lesson specifies reference geometries and a validation plan.
- **Rights:** DOI, publisher, institutional and author-hosted links only; no third-party paper text or figures reproduced.
- **Remaining work:** inspect exact algorithm variants and mesh degeneracies in greater depth; build a graph-Dijkstra baseline first, then evaluate a validated exact geodesic library and a separate fast-marching implementation.


## Section 10 — Discrete global grids and spherical indexing

**Source entry:** “Spherical and discrete global grids: ISEA3H, rHEALPix, DGGRID, hierarchical triangular mesh (HTM), hexagonal grid operations” (source page 21).

- **Standards source:** the Open Geospatial Consortium's [OGC API — Discrete Global Grid Systems, Part 1: Core](https://docs.ogc.org/is/21-038r1/21-038r1.html) defines DGGS concepts and includes an ISEA3H DGGRS definition. Its ISEA3H description explicitly identifies hexagonal and pentagonal zones and specifies the area relationship between them.
- **ISEA3H bibliography:** Sahr, K., White, D. and Kimerling, A. J. (2003), “Geodesic Discrete Global Grid Systems,” *Cartography and Geographic Information Science*, 30(2), 121–134. The source describes the icosahedral Snyder equal-area projection and aperture-3 hexagonal construction; the OGC definition records the twelve smaller pentagonal zones.
- **rHEALPix bibliography:** Gibb, R. G. (2016), “The rHEALPix Discrete Global Grid System,” *IOP Conference Series: Earth and Environmental Science*, 34, 012012, DOI [10.1088/1755-1315/34/1/012012](https://doi.org/10.1088/1755-1315/34/1/012012). The paper describes cell geometries, identifiers and topological operations.
- **HTM bibliography:** Szalay, A. S., Gray, J., Fekete, G., Kunszt, P. Z., Kukol, P. Z. and Thakar, A. (2005), “Indexing the Sphere with the Hierarchical Triangular Mesh,” Microsoft Research Technical Report MSR-TR-2005-123. The institutional record describes recursive spherical-triangle subdivision and multi-resolution indexing.
- **DGGRID and implementation comparison:** Kmoch et al. (2022), “Applied open-source Discrete Global Grid Systems,” *AGILE GIScience Series*, 3, 41, DOI [10.5194/agile-giss-3-41-2022](https://doi.org/10.5194/agile-giss-3-41-2022), compares open-source DGGS software APIs. The lesson distinguishes DGGRID as software from a named cell tessellation.
- **Technical-claim status:** the lesson distinguishes hierarchy, cell geometry, equal-area properties, addressing and query covering. It does not claim all DGGS cells are equal-area or that a cell-cover approximation replaces an exact geometry predicate.
- **Implementation:** no new DGGS or HTM implementation is claimed.
- **Rights:** standards, DOI, institutional and author-hosted links only; no third-party figures or text reproduced.
- **Remaining work:** independently test one named implementation, inspect the exact DGGRID version and supported operations, and benchmark cell assignment, hierarchy, neighbour traversal, polygon covering and query performance on the intended data.


## Section 10 — Change-point detection

**Source entry:** “Change-point detection: CUSUM, PELT, binary segmentation, BEAST, Bayesian online change-point detection” (source page 21).

- **CUSUM bibliography:** Page, E. S. (1954), “Continuous Inspection Schemes,” *Biometrika*, 41(1–2), 100–115, DOI [10.1093/biomet/41.1-2.100](https://doi.org/10.1093/biomet/41.1-2.100).
- **PELT bibliography:** Killick, R., Fearnhead, P. and Eckley, I. A. (2012), “Optimal Detection of Changepoints With a Linear Computational Cost,” *Journal of the American Statistical Association*, 107(500), 1590–1598, DOI [10.1080/01621459.2012.737745](https://doi.org/10.1080/01621459.2012.737745). The publisher abstract describes the penalised segmentation objective and linear cost under mild conditions.
- **BOCPD bibliography:** Adams, R. P. and MacKay, D. J. C. (2007), “Bayesian Online Changepoint Detection,” arXiv:0710.3742. The author-hosted paper describes online inference over the run-length distribution.
- **BEAST bibliography:** Zhao, K. et al. (2019), “Detecting change-point, trend, and seasonality in satellite time series data to track abrupt changes and nonlinear dynamics: A Bayesian ensemble algorithm,” *Remote Sensing of Environment*, DOI [10.1016/j.rse.2019.04.034](https://doi.org/10.1016/j.rse.2019.04.034). The publisher record describes Bayesian model averaging for joint change, trend and seasonal decomposition.
- **Technical-claim status:** the lesson distinguishes online monitoring, greedy recursive segmentation, penalised offline optimisation, Bayesian run-length inference and Bayesian ensemble decomposition. It qualifies PELT's linear-time claim and warns about seasonality, autocorrelation, missing observations and spatial multiple testing.
- **Implementation:** no new detector implementation is claimed.
- **Rights:** DOI and author-hosted paper links only; no source text or figures reproduced.
- **Remaining work:** verify binary segmentation's exact variant and stopping rule; add executable baseline implementations and calibrate false alarms, boundary error and detection delay on simulated and spatially structured series.


## Section 10 — Trend, seasonality and forecasting methods

**Source entry:** “Trend and seasonality: STL, seasonal-trend decomposition, Prophet, Theil-Sen, Pettitt test, ARIMA, Kalman filtering of EO series” (source page 21).

- **STL bibliography:** Cleveland, R. B., Cleveland, W. S., McRae, J. E. and Terpenning, I. (1990), “STL: A Seasonal-Trend Decomposition Procedure Based on Loess,” *Journal of Official Statistics*, 6(1), 3–73. The statsmodels and Forecasting: Principles and Practice documentation provide current implementation/teaching references.
- **Theil–Sen bibliography:** Sen, P. K. (1968), “Estimates of the Regression Coefficient Based on Kendall's Tau,” *Journal of the American Statistical Association*, 63(324), 1379–1389, DOI [10.1080/01621459.1968.10480934](https://doi.org/10.1080/01621459.1968.10480934). The publisher abstract confirms the median-of-pairwise-slopes estimator.
- **Pettitt bibliography:** Pettitt, A. N. (1979), “A Non-Parametric Approach to the Change-Point Problem,” *Journal of the Royal Statistical Society: Series C*, 28(2), 126–135, DOI [10.2307/2346729](https://doi.org/10.2307/2346729). The publisher record confirms the non-parametric single change-point testing scope.
- **ARIMA bibliography:** Box, G. E. P., Jenkins, G. M., Reinsel, G. C. and Ljung, G. M. (2015), *Time Series Analysis: Forecasting and Control*, 5th ed., Wiley.
- **Prophet bibliography:** Taylor, S. J. and Letham, B. (2018), “Forecasting at Scale,” *The American Statistician*, 72(1), 37–45, DOI [10.1080/00031305.2017.1380080](https://doi.org/10.1080/00031305.2017.1380080). The publisher abstract describes the decomposable trend/seasonality/event approach and analyst-in-the-loop forecasting.
- **Kalman filter bibliography:** Kalman, R. E. (1960), “A New Approach to Linear Filtering and Prediction Problems,” *Journal of Basic Engineering*, 82(1), 35–45, DOI [10.1115/1.3662552](https://doi.org/10.1115/1.3662552).
- **Technical-claim status:** the lesson distinguishes decomposition, robust slope estimation, a single non-parametric change-point test, autoregressive forecasting, decomposable forecasting and latent-state filtering. It warns about autocorrelation, irregular sampling, missing observations, temporal leakage and spatial dependence.
- **Implementation:** no new time-series implementation is claimed.
- **Rights:** DOI, publisher and official documentation links only; no third-party figures or text reproduced.
- **Remaining work:** build separate tested implementations; verify the STL parameter conventions and Prophet changepoint priors; evaluate ARIMA and Kalman models against baselines using rolling-origin and spatial holdout designs.


## Section 10 — Forecast verification and probabilistic scoring

**Source entries:** “Fractions Skill Score, neighborhood verification, SAL (structure, amplitude, location), object-based verification (MODE)” and “ETS, POD, FAR, CSI, Brier skill score, ROC and AUC, CRPS decomposition, rank histograms” (source page 21).

- **Fractions Skill Score:** Roberts, N. (2008), “Assessing the spatial and temporal variation in the skill of precipitation forecasts from an NWP model,” *Meteorological Applications*, 15, 163–169, DOI [10.1002/met.57](https://doi.org/10.1002/met.57). Publisher abstract confirms scale-selective FSS evaluation.
- **SAL:** Wernli, H., Paulat, M., Hagen, M. and Frei, C. (2008), “SAL—A Novel Quality Measure for the Verification of Quantitative Precipitation Forecasts,” *Monthly Weather Review*, 136, 4470–4487, DOI [10.1175/2008MWR2415.1](https://doi.org/10.1175/2008MWR2415.1). The publisher abstract identifies the structure, amplitude and location components.
- **MODE:** Davis, C., Brown, B. and Bullock, R. (2006), “Object-Based Verification of Precipitation Forecasts. Part I: Methodology and Application to Mesoscale Rain Areas,” *Monthly Weather Review*, 134, 1772–1784, DOI [10.1175/MWR3145.1](https://doi.org/10.1175/MWR3145.1).
- **Proper scoring rules:** Gneiting, T. and Raftery, A. E. (2007), “Strictly Proper Scoring Rules, Prediction, and Estimation,” *Journal of the American Statistical Association*, 102(477), 359–378, DOI [10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437). The paper develops the theory of proper scoring rules, including CRPS.
- **Technical-claim status:** the lesson separates event contingency metrics, probability calibration/discrimination, full-distribution scoring, spatial neighbourhood verification and object-based diagnostics. It explicitly warns that AUC does not measure calibration and that FSS/SAL/MODE depend on spatial and object-definition choices.
- **Implementation:** no new forecast-verification implementation is claimed.
- **Rights:** DOI and publisher links only; no third-party text or figures reproduced.
- **Remaining work:** implement scores with hand-calculated fixtures; validate edge cases such as zero denominators, event prevalence and ensemble ties; add spatially aware uncertainty intervals and reproducible forecast/observation examples.


## Section 10 — Optical flow and image motion

**Source entry:** “Optical flow for advection: Lucas-Kanade, Farneback, DIS, variational optical flow” (source page 21).

- **Lucas–Kanade bibliography:** Lucas, B. D. and Kanade, T. (1981), “An Iterative Image Registration Technique with an Application to Stereo Vision,” *Proceedings of the Seventh International Joint Conference on Artificial Intelligence*, 674–679. The IJCAI proceedings record confirms the paper and its gradient-based registration method.
- **Farnebäck bibliography:** Farnebäck, G. (2003), “Two-Frame Motion Estimation Based on Polynomial Expansion,” *Scandinavian Conference on Image Analysis*, 363–370. The author-hosted paper describes local quadratic polynomial expansion and displacement estimation.
- **DIS bibliography:** Kroeger, T., Timofte, R., Dai, D. and Van Gool, L. (2016), “Fast Optical Flow using Dense Inverse Search,” *European Conference on Computer Vision*, 471–488, DOI [10.1007/978-3-319-46493-0_29](https://doi.org/10.1007/978-3-319-46493-0_29). The paper describes inverse patch search, dense aggregation and variational refinement.
- **Implementation reference:** OpenCV's official optical-flow and DIS documentation identifies available functions, parameters and presets. The lesson treats these as implementation references, not substitutes for the original algorithm papers.
- **Technical-claim status:** the lesson distinguishes sparse/local Lucas–Kanade tracking from dense Farnebäck and DIS flow, derives the brightness-constancy constraint, and explains the affine conversion from pixel displacement to map displacement. It warns that image motion is not automatically physical surface motion.
- **Implementation:** no new optical-flow or variational-flow implementation is claimed.
- **Rights:** publisher, conference, author-hosted and official documentation links only; no third-party figures or code reproduced.
- **Remaining work:** add a tested synthetic image-pair package, evaluate occlusion and textureless regions, and verify pixel-to-map conversion on rotated and sheared georeferenced rasters.
