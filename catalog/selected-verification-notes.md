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
