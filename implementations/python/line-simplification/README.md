# Line simplification implementation

Teaching implementations for open planar polylines: Douglas–Peucker (maximum-deviation split), Visvalingam–Whyatt (least-effective-area elimination), Reumann–Witkam (moving infinite strip), Lang (bounded look-ahead with finite-segment deviation checks), Opheim (constrained moving strip with minimum/maximum search radii), and Zhao–Saalfeld (narrow-sleeve sector-bound simplification).

Run python -m pip install -r requirements.txt and python -m pytest -q from this directory.

Distance tolerances use coordinate units; Visvalingam–Whyatt uses squared coordinate units. Lang lookahead is a count of source vertices. Use projected planar coordinates. These methods do not preserve topology across coverages or coordinate shared arcs.  Reumann–Witkam and Lang have published variants; the implemented conventions are explicit in their function contracts.


## Regression coverage expansion

The test suite also checks the strict Douglas–Peucker threshold boundary, coincident endpoints, endpoint/order preservation, the squared-coordinate-unit interpretation of the Visvalingam–Whyatt area threshold, repeated vertices, and empty/singleton inputs across all six functions.

These tests document implementation contracts; they do not establish topology preservation or equivalence with every published/software variant.
