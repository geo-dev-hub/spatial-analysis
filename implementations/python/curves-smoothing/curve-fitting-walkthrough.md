# Intern walkthrough: Schneider cubic Bezier fitting

Schneider's algorithm fits a piecewise cubic Bezier curve to an ordered digitised point sequence.

1. Estimate endpoint tangents from the first and last point differences.
2. Assign each sample a chord-length parameter u in [0,1].
3. Fix the first and last Bezier controls at the endpoint samples. Solve a 2x2 least-squares system for the two tangent handle lengths.
4. Evaluate the cubic at the assigned parameters and find the maximum squared residual.
5. If the error is within tolerance, accept the segment. If it is close, attempt a small number of Newton–Raphson reparameterisations and refit.
6. Otherwise split at the maximum-error sample, estimate a centre tangent and recursively fit the two subcurves.

The requested tolerance is a squared coordinate-unit error, matching the source algorithm's convention. The fitter preserves sample endpoints and joins adjacent cubic segments at the split sample. It does not guarantee tangent continuity across splits and is not a topology-preserving polyline simplifier.

Primary reference: Philip J. Schneider (1990), “An Algorithm for Automatically Fitting Digitized Curves,” in *Graphics Gems*, pp. 612–626. The original Graphics Gems source implementation is available under its repository's stated license; this Python implementation is an independent teaching translation of the published method.
