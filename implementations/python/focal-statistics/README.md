# Focal mean with integral images

A focal mean replaces each raster cell with the mean of values in a neighbourhood around it. This implementation uses summed-area tables (integral images) for values and valid-cell counts.

## Run

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

## Example

~~~python
import numpy as np
from focal_statistics import focal_mean

raster = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
means, counts = focal_mean(raster, window_size=3)
~~~

## Contract and limits

- The raster must be a non-empty 2D array.
- Window size must be a positive odd integer.
- Windows are centred on each cell and truncated at raster edges; no padding is introduced.
- Non-finite values, a supplied NoData sentinel and cells excluded by valid_mask are ignored.
- The function returns both the focal mean and the number of valid cells contributing to each mean.
- A mean is NaN when fewer than min_count valid cells are present.
- This is a rectangular square-window mean, not a general convolution engine or a weighted focal filter.

Read the [canonical lesson](../../../algorithms/raster/focal-statistics.md) and [intern walkthrough](implementation-walkthrough.md).
