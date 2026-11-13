# Intern walkthrough: two-step floating catchment area

## 1. Define the two sides of the problem

The model has population locations and service providers. Each provider has a supply measure—such as beds, staff or service capacity—and each population location has a demand measure.

An impedance matrix links the two: rows are population locations, columns are providers. Its values may be travel time, distance or another documented cost.

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
