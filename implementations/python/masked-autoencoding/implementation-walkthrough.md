# Intern walkthrough: masked patch selection and restoration

## 1. Understand the input tensor

The input is a three-dimensional array: batch, patch sequence, feature dimension. The code does not convert an image into patches. A vision model would normally perform patch embedding before this function receives tokens.

## 2. Select visible positions

For each batch item, the function samples one random value per patch, sorts those values, and keeps the first fraction determined by the mask ratio. The random seed controls reproducibility.

The encoder in a conventional MAE receives only the visible tokens. This reduces encoder computation when the mask ratio is high.

## 3. Record the inverse permutation

Sorting the random values changes patch order. The inverse permutation records how to return to original order. This is why the result includes both kept_indices and restore_indices.

## 4. Construct the original-order mask

A shuffled mask starts with zeros for visible positions and ones for hidden positions. Applying the inverse permutation returns a mask aligned with the original patch sequence.

## 5. Restore a decoder sequence

The restoration function concatenates visible tokens with one mask token for each hidden position, then uses restore_indices to put the sequence back in original order. A real decoder would add positional information and predict the missing patch content; this example does not do either.

## 6. Geospatial design questions

For satellite imagery, consider temporal consistency, spectral band groups, sensor-specific band meaning, ground sample distance, cloud masks and spatial leakage. SatMAE and Scale-MAE are examples of research that adapts masked autoencoding to temporal/multispectral structure and known spatial scale. Read their original papers before attempting to reproduce them.

## 7. Extend the exercise

Implement a mask shared across time for a sequence of satellite acquisitions, then implement independent per-date masking. Compare which temporal information each strategy makes visible. Write tests for both and explain which downstream task each might suit.
