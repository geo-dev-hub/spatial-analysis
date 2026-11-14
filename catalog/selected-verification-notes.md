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
