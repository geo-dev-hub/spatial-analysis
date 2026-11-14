# Implementation walkthrough: methane plume algorithms

## 1. Matched filtering

Assume a local residual image d consists of a scaled known template t plus white Gaussian noise. Least squares minimises ||d-a t||². Differentiating with respect to a gives

a_hat = (d dot t)/(t dot t).

Under noise standard deviation sigma, the matched-filter detection score is

S = (d dot t)/(sigma sqrt(t dot t)).

The implementation slides each odd-sized template over the image, computes the score and amplitude, and retains the strongest template at each location. A bank can span widths and orientations. The score is not a calibrated false-alarm probability when the background is spatially correlated, the templates are selected adaptively, or noise varies across the image.

Complexity is O(K H W h w) for K templates of h-by-w pixels over an H-by-W image; FFT correlation or whitening may be needed for large template banks.

## 2. Integrated mass enhancement

The estimator Q = IME U/L is a compact mass-balance approximation. IME is an integrated excess mass, U a representative wind speed and L a characteristic plume length. It is only as defensible as those inputs and the geometric interpretation of L. Do not substitute wind speed or plume length from unrelated sources without checking co-location and time.

## 3. Cross-sectional flux

For a cross-section discretised into strips, each strip transports C_i u_i ds_i mass per time. Summing strips approximates the line integral of concentration enhancement times normal wind. The sign convention follows the supplied normal wind; widths must be positive.

## 4. What is not implemented

Raw spectral retrieval, cloud screening, wind retrieval, uncertainty propagation and operational quality control remain distinct tasks. Local median/MAD background estimation, classical hysteresis segmentation and fixed-geometry Gaussian column-plume inversion have bounded teaching implementations, but they do not replace physical retrieval or operational validation. A matched-filter score alone is not an emission estimate.


## 5. Hysteresis segmentation

Let `I_s` be the optionally smoothed enhancement field. Form a low-threshold mask `L = I_s ≥ τ_low` and a high-threshold seed mask `H = I_s ≥ τ_high`, with `τ_high ≥ τ_low`. Label connected components of `L`; retain component C exactly when `C ∩ H` is non-empty and its area meets the minimum-area rule. This is connected-component hysteresis segmentation. It reduces isolated weak detections but remains sensitive to thresholds, smoothing, connectivity and structured background. It is not a learned segmentation model.


## 6. Robust local background estimation

For each pixel, estimate a local median background `b(x)` over an odd square window. Compute residual `r(x)=I(x)-b(x)`, then estimate local robust noise scale as `s(x)=1.4826 median(|r|)` in the same window. The standardized enhancement is `r(x)/max(s(x), s_min)`, where the positive scale floor `s_min` avoids division by zero. The window-scale assumption is critical: broad plume structures may be absorbed into the median background, while small windows can treat plume pixels as anomalies.
