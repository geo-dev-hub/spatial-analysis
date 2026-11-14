# Potential-field matched bandpass decomposition

The matched_bandpass_decomposition function separates a regular grid into equivalent-layer components using a supplied radial spectral model. For each layer, the model amplitude is B * k^n * exp(-k*z); the transfer function is that layer's amplitude divided by the sum across layers.

The caller supplies positive B, non-negative depth z and n in {-1, 0, 1}. The implementation does not estimate layer parameters from the observed spectrum. It uses radians per coordinate unit, a regular-grid 2D FFT and a documented DC convention: the mean is assigned to the selected dc_layer.

This is an amplitude matched-bandpass teaching baseline. It is not a full Phillips/USGS workflow: radial-spectrum fitting, nonlinear model refinement, azimuthal filtering, windowing and physical interpretation remain external review steps. See matched-filtering-walkthrough.md and the synthetic tests.
