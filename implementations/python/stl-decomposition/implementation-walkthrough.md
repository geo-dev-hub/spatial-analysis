# Intern walkthrough: STL

STL estimates the additive decomposition y[t] = T[t] + S[t] + R[t].
It alternates LOESS smooths to estimate a slowly varying trend and a seasonal
subseries. The seasonal subseries groups observations with the same position
within each period; smoothing allows seasonal shape to evolve. A low-pass
filter helps separate seasonal and trend components. Robust iterations
reweight observations with large residuals.

This package deliberately delegates numerical LOESS and iteration machinery
to statsmodels. The local wrapper validates inputs and returns named
components. It is not an independent reimplementation. The dependency
version is part of the reproducibility record.

STL assumes regular sampling and additive components; it is not a forecast.
