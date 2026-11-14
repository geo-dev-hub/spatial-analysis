# Intern walkthrough: Boolean and fuzzy overlay

## 1. Start with the decision meaning

Boolean overlay represents conditions that are either satisfied or not satisfied. Fuzzy overlay represents graded membership in a concept. Do not switch between these meanings without explaining why.

## 2. Validate the inputs

Both functions require at least one non-empty 2D layer and matching array shapes. This check cannot establish that the rasters share the same geotransform, projection or cell alignment; that remains the caller's responsibility.

Boolean inputs must have Boolean dtype. Fuzzy inputs are converted to floating point and finite memberships must lie in [0,1].

## 3. Apply Boolean logic

The AND operation uses a cellwise logical all; OR uses a cellwise logical any. A hard exclusion can be expressed as a Boolean mask and applied separately from a suitability score.

## 4. Compare fuzzy operators

Minimum returns the weakest membership. Product compounds all memberships and is often more restrictive. Maximum returns the strongest membership. Probabilistic sum is 1 minus the product of each layer's complement.

## 5. Understand gamma

Gamma raises the probabilistic sum to gamma and the product to one minus gamma. The endpoints are useful checks: gamma=0 is product; gamma=1 is probabilistic sum. Changing gamma changes the model's balance between restrictive and permissive behaviour.

## 6. Handle missing values

The implementation marks a cell NoData if any input layer is non-finite. This prevents the set of contributing criteria from changing silently across the map, but it may discard cells with partial coverage.

## 7. Tests and extension work

Tests cover Boolean truth tables, each fuzzy operator, gamma endpoints, invalid parameters, shape/range contracts and strict NoData propagation.

Extension: implement a linear fuzzy membership ramp with documented breakpoints, plot the curve, and ask domain experts whether the chosen breakpoints make sense before running a regional analysis.
