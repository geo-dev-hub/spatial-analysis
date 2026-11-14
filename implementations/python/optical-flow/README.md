# Optical flow: Lucas–Kanade, Farnebäck and DIS

This package contains three executable optical-flow treatments:

- A single-scale dense local Lucas–Kanade teaching implementation.
- An OpenCV-backed Farnebäck dense-flow wrapper based on polynomial expansion.
- An OpenCV-backed DIS dense inverse-search wrapper with explicit speed/quality preset and refinement parameters.

## Install and run

    python -m pip install -r requirements.txt
    python -m pytest -q

## Coordinate and image contract

Inputs are equally shaped, finite, single-channel 2D image frames on the same pixel grid. The dense wrappers convert numeric inputs to 8-bit grayscale by clipping to [0,255]; scale and normalise scientific imagery deliberately before calling them. Output u is horizontal column displacement and v is vertical row displacement from the first frame toward the second. The flow is in pixels, not map units.

For a georeferenced raster, convert (u,v) using the raster affine linear transform. Do not interpret apparent image motion as physical ground motion without accounting for platform motion, orthorectification, terrain parallax, acquisition interval and image formation.

## Farnebäck

The wrapper calls OpenCV's calcOpticalFlowFarneback and exposes pyramid scale, levels, window size, iterations, polynomial neighbourhood and sigma. It is a library-backed implementation, not a from-scratch reproduction of the polynomial expansion method.

## DIS

The wrapper calls OpenCV's DISOpticalFlow implementation and exposes the ultrafast, fast and medium presets, finest scale, patch size/stride, gradient-descent iterations and variational-refinement toggle. It is a library-backed implementation, not a from-scratch reproduction of the inverse-search algorithm.

## Tests

Synthetic translated texture fixtures check the direction and approximate magnitude of both dense flow fields. Invalid input and parameter contracts are also tested. These fixtures do not constitute a broad benchmark across occlusion, radiometric change, large motion, textureless regions or real satellite sequences.

See the [method-selection guide](../../../methods/optical-flow.md) for assumptions, failure modes and evaluation recommendations.
