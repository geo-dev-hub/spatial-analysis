# Population diversity and segregation statistics

Teaching implementations for:
- Shannon entropy and Simpson concentration on count arrays;
- Reardon–Firebaugh multigroup entropy segregation index;
- group exposure matrix and diagonal isolation probabilities.

Counts are non-negative and finite. The segregation and exposure functions require positive population in every included areal unit and positive totals for every included group. The exposure matrix uses areal-unit composition and does not include distance, adjacency or spatial interaction weights. It is not a spatially explicit exposure model.

Run python -m pip install -r requirements.txt and python -m pytest -q.
