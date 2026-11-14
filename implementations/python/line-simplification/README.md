# Line simplification implementation

Teaching implementations for open planar polylines: Douglas–Peucker (maximum-deviation split), Visvalingam–Whyatt (least-effective-area elimination), Reumann–Witkam (moving infinite strip), Lang (bounded look-ahead with finite-segment deviation checks), and Opheim (constrained moving strip with minimum/maximum search radii).

Run python -m pip install -r requirements.txt and python -m pytest -q from this directory.

Distance tolerances use coordinate units; Visvalingam–Whyatt uses squared coordinate units. Lang lookahead is a count of source vertices. Use projected planar coordinates. These methods do not preserve topology across coverages or coordinate shared arcs. Zhao–Saalfeld remains outside this package. Reumann–Witkam and Lang have published variants; the implemented conventions are explicit in their function contracts.
