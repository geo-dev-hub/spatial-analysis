# How the IDW implementation works

## 1. Check the observations

The validation function checks that at least one observation exists, that every point has the same coordinate dimension and that each point has one finite value.

## 2. Check the target and parameters

The target must have the same dimension. The power must be finite and positive. If supplied, the neighbour count must be a positive integer and the search radius must be positive.

## 3. Measure distances

For a two-dimensional Cartesian coordinate system:

$$
d(s_0,s_i)=\sqrt{(x_0-x_i)^2+(y_0-y_i)^2}.
$$

The code generalises this to any fixed number of dimensions. It does not know whether coordinates are metres, feet or degrees; the caller must choose a meaningful coordinate system.

## 4. Handle an exact location

The inverse-distance expression is undefined at zero distance. If the target matches an observation, the implementation returns the observed value. If multiple records occupy that coordinate, it averages them. This duplicate policy is explicit and tested.

## 5. Choose the contributing observations

A supplied radius removes points outside that distance. The remaining points are sorted by distance. If `max_neighbors` is supplied, only the nearest requested number are retained. Without either option, every observation contributes.

## 6. Calculate normalized weights

The formula uses weights proportional to $d_i^{-p}$. Scaling all raw weights by the same positive constant does not change the normalized result, so the implementation uses:

$$
w_i=\left(\frac{d_{\\min}}{d_i}\right)^p.
$$

The normalized weights are $\\lambda_i=w_i/\\sum_jw_j$. This keeps the largest raw weight equal to one.

## 7. Calculate the weighted average

$$
\\hat z(s_0)=\\frac{\\sum_iw_i z(s_i)}{\\sum_iw_i}.
$$

Because all weights are positive, the estimate lies between the smallest and largest contributing observations.

## 8. What the tests check

Tests cover the hand-calculated example, exact hits, coincident observations, power changes, neighbourhood restrictions, invalid inputs, constant values, translation invariance and the weighted-average range property. They do not establish that IDW is appropriate for a particular dataset. Predictive performance must be assessed using withheld observations and a validation design suited to spatial dependence.

## Reproduce

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
