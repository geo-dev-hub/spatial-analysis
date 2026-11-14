"""Spectral matched-bandpass separation of potential-field source ensembles."""
from __future__ import annotations
import numpy as np


def matched_bandpass_decomposition(grid, dx, dy, layers, *, dc_layer=0):
    """Separate a regular grid using a supplied equivalent-layer spectral model.

    Each layer is a mapping with positive amplitude B, non-negative depth z
    and spectral exponent n in {-1, 0, 1}. Its radial amplitude model is
    B * k**n * exp(-k*z), where k is radial angular wavenumber. The filter
    for layer j is its model amplitude divided by the sum across layers.

    This bounded implementation does not fit equivalent layers, infer their
    geological meaning, or design azimuthal filters. Frequencies use radians
    per coordinate unit. The caller must supply positive grid spacings in a
    suitable planar coordinate system.

    The DC coefficient is assigned wholly to dc_layer so that the component
    grids preserve the input mean and sum to the input grid.
    """
    data = np.asarray(grid, dtype=float)
    if data.ndim != 2 or min(data.shape) < 4 or not np.all(np.isfinite(data)):
        raise ValueError("grid must be a finite 2D array with each dimension >= 4")
    dx, dy = float(dx), float(dy)
    if not np.isfinite(dx) or not np.isfinite(dy) or dx <= 0 or dy <= 0:
        raise ValueError("dx and dy must be finite and positive")
    if not isinstance(layers, (list, tuple)) or len(layers) < 2:
        raise ValueError("at least two equivalent layers are required")
    parsed = []
    for layer in layers:
        if not isinstance(layer, dict) or not {"B", "z", "n"} <= set(layer):
            raise ValueError("each layer must provide B, z and n")
        amplitude, depth, exponent = float(layer["B"]), float(layer["z"]), layer["n"]
        if not np.isfinite(amplitude) or amplitude <= 0:
            raise ValueError("layer B values must be finite and positive")
        if not np.isfinite(depth) or depth < 0:
            raise ValueError("layer z values must be finite and non-negative")
        if isinstance(exponent, bool) or exponent not in (-1, 0, 1):
            raise ValueError("layer n must be one of -1, 0 or 1")
        parsed.append((amplitude, depth, int(exponent)))
    if isinstance(dc_layer, bool) or not isinstance(dc_layer, (int, np.integer)) or not 0 <= dc_layer < len(parsed):
        raise ValueError("dc_layer must be a valid layer index")

    ky = 2 * np.pi * np.fft.fftfreq(data.shape[0], d=dy)
    kx = 2 * np.pi * np.fft.fftfreq(data.shape[1], d=dx)
    radial_k = np.sqrt(ky[:, None] ** 2 + kx[None, :] ** 2)
    positive = radial_k > 0
    k_floor = float(np.min(radial_k[positive]))
    safe_k = np.where(positive, radial_k, k_floor)

    models = []
    for amplitude, depth, exponent in parsed:
        models.append(amplitude * np.power(safe_k, exponent) * np.exp(-safe_k * depth))
    models = np.stack(models, axis=0)
    denominator = np.sum(models, axis=0)
    if not np.all(np.isfinite(denominator)) or np.any(denominator <= 0):
        raise ValueError("equivalent-layer spectral model is numerically invalid")
    filters = models / denominator[None, :, :]
    filters[:, ~positive] = 0.0
    filters[dc_layer, ~positive] = 1.0

    spectrum = np.fft.fft2(data)
    components = np.stack([
        np.fft.ifft2(spectrum * filters[index]).real
        for index in range(len(parsed))
    ])
    return {
        "components": components,
        "filters": filters,
        "layers": tuple({"B": b, "z": z, "n": n} for b, z, n in parsed),
        "dc_layer": int(dc_layer),
        "reconstruction": components.sum(axis=0),
    }
