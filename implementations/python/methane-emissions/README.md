# Methane plume detection and emission-rate baselines

This package starts after retrieval: the input is a finite 2D enhancement field or a sampled cross-section in physical units. It does not process raw satellite radiance, perform atmospheric correction, retrieve methane columns, estimate wind, or validate operational plume products.

## Matched-filter plume detection

A template t is correlated with the residual field. The least-squares amplitude estimate is <d,t>/<t,t>, and the standardized matched-filter score is <d,t>/(sigma ||t||). A bank of templates can represent different plume widths and orientations. The maximum-scoring template is retained per pixel. The method assumes approximately white, zero-mean Gaussian residual noise; correlated backgrounds and spatially varying noise require whitening or a more explicit covariance model.

The Gaussian templates are convenient synthetic plume shapes, not a substitute for a physically complete plume forward model.

## Integrated mass enhancement (IME)

The simple crosswind integrated-mass estimator is

Q = IME * U / L,

where IME is integrated excess mass (kg), U is representative wind speed (m/s), and L is a characteristic plume length (m). The result is kg/s. The definition and retrieval of IME, wind and L must be documented for real observations; this function only performs the stated dimensional calculation.

## Cross-sectional flux

For sampled concentration enhancement C_i, normal wind u_i and segment width ds_i,

Q = sum_i C_i u_i ds_i.

With C in kg/m^3, u in m/s and ds in m, Q is kg/s. Normal wind is signed, so reversing the flow reverses flux.

## Validation

Synthetic tests check matched-filter localization and amplitude recovery, template selection, invalid inputs, dimensional IME arithmetic and signed cross-sectional integration. These tests validate the code contract, not the accuracy of a satellite emissions product.

Run `python -m pip install -r requirements.txt` and `python -m pytest -q`.
