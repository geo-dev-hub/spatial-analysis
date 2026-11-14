# Intern walkthrough: two-step floating catchment area

## 1. Define the two sides of the problem

The model has population locations and service providers. Each provider has a supply measure—such as beds, staff or service capacity—and each population location has a demand measure.

An impedance matrix links the two: rows are population locations, columns are providers. Its values may be travel time, distance or another documented cost. Positive infinity can represent a pair with no route; NaN and negative values are rejected.

## 2. Step one: calculate provider supply-to-demand ratios

For provider $j$, collect all population locations inside the catchment and calculate:

$$
R_j=\frac{S_j}{\sum_{i:d_{ij}\leq d_0}P_i}
$$

Here $S_j$ is provider supply, $P_i$ is population demand, $d_{ij}$ is impedance and $d_0$ is the catchment threshold.

A provider with no population in its catchment receives a zero ratio in this implementation. This is an explicit computational convention for an otherwise undefined ratio.

## 3. Step two: sum reachable provider ratios

For population location $i$:

$$
A_i=\sum_{j:d_{ij}\leq d_0}R_j
$$

The result is a relative accessibility score under the chosen catchment and impedance model. It is not a probability of receiving service or a direct measure of service quality.

## 4. Make the threshold visible

The code uses an inclusive binary catchment: a provider is reachable when impedance is less than or equal to max_cost. A different threshold can change both provider ratios and the accessibility score.

Enhanced 2SFCA variants introduce distance-decay weights, multiple catchments or other competition assumptions. They are not implemented here.

## 5. Validate the interpretation

Check the units and meaning of supply and demand. A provider count is not necessarily comparable to service capacity. Population counts should match the relevant time period. Road travel time and transit travel time define different access opportunities.

The tests cover a known two-provider example, inclusive thresholds, isolated providers, zero supply and invalid inputs. They validate the implementation, not the suitability of the model for a policy decision.


## 6. Extend the method with distance decay

The binary method gives every pair inside the threshold the same weight. E2SFCA replaces that all-or-nothing contribution with a weight that declines across travel-time or distance bands. Luo and Qi (2009) apply the weights in both stages, not only when calculating the final population score.

For population location \(i\) and provider \(j\), define \(w_{ij}\) from the supplied band schedule. Then:

\[
R_j=\frac{S_j}{\sum_i P_i w_{ij}},
\qquad
A_i=\sum_j R_j w_{ij}.
\]

The code accepts the upper edge of each band and its weight. The upper edges must increase; weights must be non-negative and non-increasing. A pair beyond the final edge has weight zero. The same weight matrix is used in both stages.

### Reproduce the worked calculation

For costs \(\begin{bmatrix}5&15\\25&5\end{bmatrix}\), band edges \([10,20]\), and weights \([1,0.5]\), the weight matrix is:

\[
W=\begin{bmatrix}1&0.5\\0&1\end{bmatrix}.
\]

With supplies \([10,20]\) and demands \([100,100]\), weighted demand by provider is \([100,150]\). The provider ratios are \([0.1,0.1333\ldots]\), and population accessibility is approximately \([0.1667,0.1333]\).

Run the tests to verify both the numerical result and edge behaviour: values exactly on band boundaries, values outside the final band, malformed band schedules and monotonicity violations.

### Interpret the weights rather than copying them

The implementation deliberately requires the analyst to provide band edges and weights. It does not prescribe a universal travel-time schedule. A 10-minute interval may mean something different for walking, driving, public transport, rural services or emergency care. Test alternative schedules and report how the ranking or spatial pattern changes.
