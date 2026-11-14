# Intern walkthrough: covariance functions

## 1. Start with the modelling question

A covariance function describes how strongly two values are expected to vary together as their locations change. Before coding, identify the domain, coordinate system, units, support and intended prediction task. A distance formula is not automatically a valid covariance model on every geometry.

## 2. Inspect the package

- `covariance.py` evaluates five named Euclidean covariance models, builds a dense matrix and reports basic eigenvalue diagnostics.
- `test_covariance.py` checks symmetry, diagonal variance, selected positive-semidefinite fixtures, compact support, duplicate sites and invalid inputs.
- `README.md` records the coordinate and model contract.

## 3. Install and run

From this directory:

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
~~~

Run the same tests from a clean environment before changing the code. Record the Python and NumPy versions if results differ.

## 4. Trace one covariance entry

For sites \(s_i\) and \(s_j\), the implementation first computes Euclidean distance \(h_{ij}=\|s_i-s_j\|\). It divides by the range scale \(a\), evaluates the selected correlation shape and multiplies by the marginal variance \(\sigma^2\). The diagonal has distance zero, so every diagonal entry equals \(\sigma^2\).

## 5. Check the matrix, not just the curve

A curve that looks plausible is not enough. A covariance matrix assembled for any finite set of sites must be symmetric and positive semidefinite. The diagnostic symmetrises only for the eigenvalue calculation, reports whether the original matrix is symmetric, and applies a stated tolerance. It does not certify a model in general.

## 6. Reproduce and extend

1. Change the range scale and predict how off-diagonal values should move.
2. Compare the five curves at the same variance and range.
3. Add a duplicate site and explain why the matrix becomes singular without becoming invalid.
4. Generate several random point sets and inspect the smallest eigenvalue.
5. Add a test before adding a new covariance family.

## 7. What not to infer

This package does not fit parameters from observations, estimate a nugget, handle anisotropy or provide kriging predictions. The spherical and network cases need geometry-specific validity theory. Do not replace great-circle distance into a familiar planar kernel and assume the result remains valid.
