# Section 10 algorithm-level completion register

This is the first algorithm-level reconciliation of the original Section 10 source (pages 21–22). It deliberately separates a named algorithm from the grouped source row that contains it. It is a working audit, not a claim that Section 10 or the compendium is complete.

**Status meanings**

- **Implemented / tested** — a corresponding executable implementation and tests are present in the repository. This does not by itself mean independent review or publication-ready completion.
- **Partial** — related code or a family lesson exists, but the named algorithm is absent, only one variant is implemented, or validation/learning material is incomplete.
- **Research / lesson only** — explanatory material exists, but no matching tested implementation is present.
- **Open** — no adequate algorithm-specific treatment has yet been verified.

A shared family lesson or notebook is not counted as a separate derivation for every child algorithm. Rights review and source-entry verification remain separate release checks.

## Rasterisation and low-level geometry — source page 21

| Source family | Child algorithm | Verified repository treatment | Status |
|---|---|---|---|
| Rasterisation | DDA line rasterisation | `implementations/python/rasterization/` implementation, tests and lab | Implemented / tested |
| Rasterisation | Bresenham line rasterisation | Same package; all-octant variant | Implemented / tested |
| Rasterisation | Wu anti-aliased line | Same package and tests | Implemented / tested |
| Rasterisation | Scanline polygon fill | Same package; centre-sampled even-odd fill | Implemented / tested |
| Rasterisation | Supercover line | Same package; closed-cell convention | Implemented / tested |
| Line clipping | Cohen–Sutherland | `implementations/python/line-clipping/`, tests and lab | Implemented / tested |
| Line clipping | Liang–Barsky | Same package, tests and lab | Implemented / tested |
| Line clipping | Cyrus–Beck | Same package; convex polygon window contract | Implemented / tested |
| Line clipping | Nicholl–Lee–Nicholl | Section 10 lesson mentions it as further reading; no implementation or dedicated test suite verified | Open |
| Line simplification | Reumann–Witkam | Moving infinite-strip teaching implementation, tests and walkthrough added; variant contract stated | Implemented / tested candidate; independent reference comparison pending |
| Line simplification | Lang | Bounded look-ahead teaching implementation, tests and walkthrough added; vertex-count lookahead contract stated | Implemented / tested candidate; independent reference comparison pending |
| Line simplification | Opheim | Family lesson exists; no implementation verified | Open |
| Line simplification | Zhao–Saalfeld | Family lesson exists; no implementation verified | Open |
| Line simplification | Visvalingam–Whyatt effective area | `implementations/python/line-simplification/` implementation and tests | Implemented / tested |
| Curves and smoothing | Chaikin corner cutting | `implementations/python/curves-smoothing/`, tests and notebook | Implemented / tested |
| Curves and smoothing | Catmull–Rom spline | Same package; uniform, centripetal and chordal parameterisations | Implemented / tested |
| Curves and smoothing | B-splines | de Boor evaluator, tests, walkthrough and spline notebook added | Implemented / tested candidate; reference review pending |
| Curves and smoothing | NURBS | Homogeneous de Boor evaluator, rational quarter-circle test and notebook added | Implemented / tested candidate; reference review pending |
| Curves and smoothing | Schneider Bezier fitting | Bezier evaluation exists, but curve-fitting algorithm is not the same deliverable | Partial |
| Curves and smoothing | Kalman smoother | Linear-Gaussian vector-state filter and RTS smoother; tests, walkthrough and notebook added | Implemented / tested candidate; model/reference review pending |
| Curves and smoothing | Rauch–Tung–Striebel smoother | Backward fixed-interval RTS pass added to tested Kalman package | Implemented / tested candidate; model/reference review pending |
| Mesh geodesics | Mitchell–Mount–Papadimitriou exact geodesics | Comparative method guide; no executable package verified | Research / lesson only |
| Mesh geodesics | Chen–Han exact geodesics | Comparative method guide; no executable package verified | Research / lesson only |
| Mesh geodesics | Fast marching on triangle meshes | Comparative method guide; no executable package verified | Research / lesson only |
| Discrete global grids | ISEA3H | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | rHEALPix | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | DGGRID | Software/tool, not a single algorithm; guide discusses it | Research / lesson only |
| Discrete global grids | Hierarchical triangular mesh (HTM) | Family guide; no algorithm implementation verified | Research / lesson only |
| Discrete global grids | Hexagonal grid operations | Family guide; no operation-specific implementation verified | Research / lesson only |

## Time series, change detection and state sequences — source page 21

| Source family | Child algorithm / method | Verified repository treatment | Status |
|---|---|---|---|
| Change points | CUSUM | Two-sided Page-style mean-shift implementation, tests and walkthrough added | Implemented / tested candidate; threshold calibration and reference review pending |
| Change points | Binary segmentation | Greedy SSE split implementation and tests added | Implemented / tested candidate; comparison review pending |
| Change points | PELT | Pruned exact SSE mean-shift implementation, brute-force partition test and walkthrough added | Implemented / tested candidate; independent reference review pending |
| Change points | BEAST | Family comparison guide; no matching implementation verified | Research / lesson only |
| Change points | Bayesian online change-point detection | Conjugate Gaussian-mean run-length recursion, tests and notebook added | Implemented / tested candidate; reference/model review pending |
| Trend / seasonality | STL decomposition | Family guide; no matching implementation verified | Research / lesson only |
| Trend / seasonality | Prophet | External software/model; family guide only | Research / lesson only |
| Trend / seasonality | Theil–Sen trend estimator | Family guide; no matching implementation verified | Research / lesson only |
| Trend / seasonality | Pettitt test | Family guide; no matching implementation verified | Research / lesson only |
| Trend / seasonality | ARIMA | Family guide; no matching implementation verified | Research / lesson only |
| Trend / seasonality | Kalman filtering of EO series | Family guide; no matching implementation verified | Research / lesson only |
| State sequences | Hidden Markov model (discrete model / filtering) | Viterbi package implements decoding, not HMM parameter estimation or full inference | Partial |
| State sequences | Viterbi decoding | `implementations/python/hmm-viterbi/`, tests, walkthrough and notebook | Implemented / tested |

## Forecast verification and motion — source page 21

| Source family | Child metric / algorithm | Verified repository treatment | Status |
|---|---|---|---|
| Spatial verification | Fractions Skill Score (FSS) | Regular-grid square-neighbourhood implementation, tests and scale notebook | Implemented / tested |
| Spatial verification | SAL | Guide discusses it; no matching implementation verified | Research / lesson only |
| Spatial verification | MODE object-based verification | Guide discusses it; no matching implementation verified | Research / lesson only |
| Categorical / probabilistic verification | ETS | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | POD | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | FAR | Tested forecast-verification package | Implemented / tested |
| Categorical / probabilistic verification | CSI | Tested forecast-verification package | Implemented / tested |
| Probabilistic verification | Brier score and Brier skill score | Tested forecast-verification package | Implemented / tested |
| Probabilistic verification | ROC and AUC | Tested forecast-verification package; tied-rank ROC AUC | Implemented / tested |
| Probabilistic verification | CRPS decomposition | Guide/context only; no matching implementation verified | Open |
| Probabilistic verification | Rank histograms | Guide/context only; no matching implementation verified | Open |
| Optical flow | Lucas–Kanade | Family guide; no matching implementation verified | Research / lesson only |
| Optical flow | Farnebäck | Family guide; no matching implementation verified | Research / lesson only |
| Optical flow | DIS | Family guide; no matching implementation verified | Research / lesson only |
| Optical flow | Variational optical flow | Family guide; no matching implementation verified | Research / lesson only |

## Spatial validation and adaptive sampling — source pages 21–22

| Source family | Child method | Verified repository treatment | Status |
|---|---|---|---|
| Spatial validation | NNDM | Research discussion distinguishes it from the implemented baselines; no NNDM implementation verified | Research / lesson only |
| Spatial validation | kNNDM | Research discussion distinguishes it from the implemented baselines; no kNNDM implementation verified | Research / lesson only |
| Spatial validation | Buffered leave-one-out | Related validation guide; no dedicated implementation verified | Partial |
| Spatial validation | Spatial k-fold by clustering | Tested spatial cross-validation package covers selected fold/block baselines; exact clustering design needs confirmation | Partial |
| Spatial validation | blockCV | External R package / method reference, not a Python algorithm to clone | Research / lesson only |
| Spatial validation | Spatial + temporal leave-out | Guide-level discussion; no matching implementation verified | Research / lesson only |
| Adaptive sampling | Bayesian optimisation on spatial fields | Family guide only; no matching implementation verified | Research / lesson only |
| Adaptive sampling | Multi-armed bandits for survey design | Family guide only; no matching implementation verified | Research / lesson only |
| Adaptive sampling | Adaptive cluster sampling | Family guide only; no matching implementation verified | Research / lesson only |
| Adaptive sampling | Active learning for map validation | Family guide only; no matching implementation verified | Research / lesson only |
| Distribution shift | Kernel two-sample tests / MMD | Family guide only; no matching implementation verified | Research / lesson only |
| Distribution shift | Energy distance | Family guide only; no matching implementation verified | Research / lesson only |
| Distribution shift | Domain-classifier divergence | Family guide only; no matching implementation verified | Research / lesson only |

## What this audit says right now

1. **There is real executable work already present.** The strongest Section 10 implementation clusters include rasterisation, three line-clipping algorithms, four line simplifiers (Douglas–Peucker, Visvalingam–Whyatt, Reumann–Witkam and Lang), three curve constructors, Viterbi decoding, CUSUM, binary segmentation, PELT mean-shift segmentation, forecast metrics and FSS.
2. **Several family guides are not algorithm completion.** Mesh geodesics, discrete global grids, change points, trend/seasonality, optical flow, adaptive sampling and distribution shift still need child-level development.
3. **Some apparent matches are deliberately marked partial.** Bezier evaluation is not Schneider fitting; Viterbi decoding is not a complete HMM estimation package; spatial cross-validation baselines are not NNDM/kNNDM.
4. **This is not yet a complete Section 10 ledger.** The original source also includes geophysical processing, microclimate, environmental monitoring, population methods and other families on pages 22–23. Those will be split into child records next. Sections 1–9 and 11–22 still need the same reconciliation.

## Immediate algorithm-first queue

1. Nicholl–Lee–Nicholl: recover the complete case classification from the original paper, implement only the documented 2D rectangular-window algorithm, and test it against a trusted clipping oracle.
2. Opheim and Zhao–Saalfeld: develop and compare each simplification algorithm separately rather than treating them as one generic simplifier.
3. B-splines and NURBS: derive basis evaluation and knot/weight behaviour before adding code.
4. BOCPD and BEAST: specify the probabilistic model, priors/hazard and computational strategy before implementation.
5. Mesh geodesics: choose a bounded reference reproduction and state the exact mesh assumptions before coding.

## Evidence consulted for the first reconciliation

- Original source transcription: [pages 21–25](../../source-inventory/pages-21-25.md).
- Repository implementation and test files are linked in the corresponding package READMEs and test modules.
- Nicholl–Lee–Nicholl identity and scope: Nicholl, Lee & Nicholl (1987), “An efficient new algorithm for 2-D line clipping: Its development and analysis,” SIGGRAPH '87, DOI [10.1145/37401.37432](https://doi.org/10.1145/37401.37432); see also the [2022 line-clipping survey](https://www.mdpi.com/2313-433X/8/10/286) and [Brown University graphics notes](https://cs.brown.edu/media/filer_public/88/9c/889c4b64-6979-4d31-a4fe-3904a681b978/dasilva.pdf).


## 14 November 2026 — implementation update

Two additional algorithm families now have executable teaching baselines and learning artefacts:

- Line simplification: Reumann–Witkam and Lang added beside Douglas–Peucker and Visvalingam–Whyatt; package tests and intern walkthrough updated; comparison notebook added.
- Change points: CUSUM, binary segmentation and PELT for piecewise-constant mean/SSE added; tests include brute-force partition comparison for PELT; walkthrough and synthetic lab notebook added.

These are implementation candidates, not independently verified release completions. Reference-equivalence checks, notebook execution in CI, rights review and technical review remain open. Opheim, Zhao–Saalfeld, BOCPD and BEAST remain open algorithm tasks.


Additional update: B-spline and NURBS evaluation by de Boor has been added to the curves package, with polynomial and rational validation fixtures, a walkthrough and a dedicated notebook. Schneider fitting and Kalman/RTS smoothing remain separate, unimplemented methods.


Further implementation update: polynomial B-spline and rational NURBS evaluation (de Boor) plus linear-Gaussian Kalman filtering and RTS smoothing are now present in the curves package, with tests, walkthroughs and dedicated notebooks. Schneider's curve fitting remains open. These are implementation candidates pending CI and independent technical/reference review.


Bayesian online change-point detection has now been added as a bounded conjugate-Gaussian teaching model with run-length posterior, change probabilities, tests and a lab notebook. BEAST remains open.
