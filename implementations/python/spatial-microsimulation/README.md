# Spatial microdata weight calibration (IPF)

This package implements iterative proportional fitting (IPF), also called raking, to calibrate weights on an existing seed micro-sample so selected categorical margins match supplied area-level controls.

For each control category, weights in that category are multiplied by target/current fitted margin. The algorithm cycles through controls until all fitted margins are within a relative tolerance or the iteration limit is reached.

## Contract and limitations

- Inputs are seed-record weights, a binary record-by-control membership matrix, and target totals in matching column order.
- Zero seed weights remain structural zeros; the method cannot invent a missing household/person type.
- Controls must be mutually compatible and have seed support. Incompatible margins may fail to converge; inspect convergence, iteration and error diagnostics.
- This calibrates weights. It does not generate new records, assign households to locations, protect privacy by itself, or solve a full spatial microsimulation.
- No uncertainty or disclosure-risk guarantee is provided.

Install dependencies with pip install -r requirements.txt and run python -m pytest -q. See the walkthrough and visual lab at ../../../notebooks/spatial-microdata-ipf-lab.ipynb.
