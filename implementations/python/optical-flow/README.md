# Lucas–Kanade optical flow

A single-scale dense local Lucas–Kanade teaching baseline for two finite, equally shaped 2D frames. It averages spatial gradients across frames, computes the temporal difference, accumulates local normal-equation terms over a square window and solves for horizontal (u/column) and vertical (v/row) displacement.

Pixels with insufficient two-direction texture are marked invalid and return NaN flow. The method assumes small motion and brightness constancy. It does not implement pyramidal warping, robust outlier rejection, Farnebäck, DIS or variational optical flow.

Run python -m pip install -r requirements.txt and python -m pytest -q. Use images on a common grid; map-coordinate flow requires conversion through the raster affine transform and CRS.
