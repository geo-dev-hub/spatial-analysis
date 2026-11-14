# Exercise: inspect a snap-rounded arrangement

Use the snap-rounding noder implementation.

1. Create two segments that cross at a non-integer coordinate. Predict the hot pixel before running the code.
2. Change the grid size and compare the hot-pixel set and resulting polylines.
3. Add a collinear overlap and identify which overlap endpoints become arrangement vertices.
4. Test a negative half-grid coordinate and explain the documented tie rule.
5. Construct a segment that lies on a hot-pixel boundary. Explain why closed pixel squares can produce multiple hits at the same projected position.
6. Compare this pairwise teaching baseline with a production snap-rounding algorithm. Discuss performance, precision and topology guarantees.

Submit the input segments, grid size, output hot pixels, per-segment polylines and a short explanation of any surprising result.
