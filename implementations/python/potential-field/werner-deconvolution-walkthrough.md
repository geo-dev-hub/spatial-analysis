# Werner 2D thin-dike deconvolution: intern walkthrough

## 1. Source model

The idealized profile anomaly of a 2D thin sheet (dike) is

\[
F(x)=\frac{A h+B(x-x_0)}{(x-x_0)^2+h^2},
\]

where x0 is the horizontal position above the top of the sheet, h is depth to its top, and A and B collect magnetic-property and orientation terms.

This is a deliberately restricted thin-dike model. It assumes an isolated residual profile, a level observation plane and a source whose strike is effectively infinite and perpendicular to the profile.

## 2. Linearization

Multiply through by the denominator and expand:

\[
x^2F=a_0+a_1x+b_0F+b_1xF,
\]

with

\[
a_0=Ah-Bx_0,\quad a_1=B,\quad
b_0=-(x_0^2+h^2),\quad b_1=2x_0.
\]

For each moving window, solve the four-coefficient linear least-squares system. Recover

\[
x_0=\frac{b_1}{2},\qquad
h=\sqrt{-b_0-x_0^2},\qquad
B=a_1,\qquad
A=\frac{a_0+a_1x_0}{h}.
\]

The implementation centers and scales each window's coordinates before solving, then converts location, depth and amplitudes back to the original coordinate units.

## 3. Moving windows

The default window contains seven observations, producing an overdetermined system. The window advances by one sample by default. Each accepted solution records its original row range, source parameters, design-matrix condition number and profile RMSE. Rank-deficient, ill-conditioned and non-positive-depth windows are rejected with reasons.

## 4. Interpretation and limits

A cluster of similar window solutions can support a coherent interpretation, but this package does not perform clustering or select a geological source automatically. It does not include regional polynomial interference, overlapping dikes, thick-interface horizontal-gradient transformation, upward continuation, remanence modelling or the nonlinear Marquardt refinement of later Werner workflows. The amplitudes A and B are model coefficients, not direct susceptibility estimates without the necessary field/orientation physics.

Use a residual profile with background removed and inspect solution stability across window sizes. Do not treat every accepted window as an independent geological body.

## References

- Werner, S. (1953). Interpretation of magnetic anomalies at sheet-like bodies. (Original thin-dike formulation; cited and reproduced in later Werner-deconvolution literature.)
- Hartman, R. R., Tesky, D. J. & Friedberg, J. L. (1971). A system for rapid digital aeromagnetic interpretation. Geophysics, 36(5), 891–918.
- Ku, C. C. & Sharp, J. A. (1983). Werner deconvolution for automated magnetic interpretation and its refinement using Marquardt's inverse modeling. Geophysics, 48(6), 754–774. https://doi.org/10.1190/1.1441505
- Werner model and practical interpretation discussion: https://pmc.ncbi.nlm.nih.gov/articles/PMC8085713/
