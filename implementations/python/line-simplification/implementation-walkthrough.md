# Intern walkthrough: four line simplification algorithms

Douglas–Peucker splits at the largest perpendicular deviation from a finite segment. Visvalingam–Whyatt repeatedly removes the vertex with the smallest effective triangle area and updates its neighbours. Reumann–Witkam scans inside a moving infinite strip and retains the last in-strip vertex when a point exits. Lang examines a bounded number of vertices ahead and retains the furthest endpoint whose finite baseline stays within tolerance of every intervening point.

All inputs are open planar polylines. Distance tolerances use coordinate units; the area threshold uses squared coordinate units. Lang lookahead is a vertex count. The algorithms are not interchangeable and none guarantees topology preservation between adjacent features.

Run the tests, then compare on digitising noise, sharp bends, reversals, repeated vertices, long lines and multiple tolerances. Inspect geometric displacement as well as vertex count.


## Algorithm 5 — Opheim

Opheim adds minimum and maximum distance constraints to a moving search corridor. This implementation defines the corridor by its perpendicular half-width and the search radii by Euclidean distance from the current anchor. It chooses the last vertex inside both constraints, retains it and restarts the search from that point. The exact width convention is made explicit because published summaries describe a corridor width but do not always state whether the tolerance is a full width or half-width.

This is an open-line teaching variant. It does not include road-network semantic constraints, topology conflict handling or the later improved Opheim variants. Compare the exact contract and test fixtures before comparing output with another software package.
