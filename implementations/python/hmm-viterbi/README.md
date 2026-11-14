# Hidden Markov models and Viterbi decoding

This package implements discrete-emission HMM maximum a posteriori sequence decoding using the Viterbi dynamic program. Supply the hidden-state order, observation alphabet, initial probabilities, row-stochastic transition matrix and state-by-symbol emission matrix. The decoder returns the most likely hidden-state sequence and its joint log probability.

Run `python -m pytest -q` from this directory. Runtime code uses only the Python standard library.

Zero probabilities are supported in log space. Unknown symbols, non-normalised probability rows, duplicate state/symbol labels and dimension mismatches raise `ValueError`. Ties resolve to the first state in the declared state order. Empty observation sequences return an empty path and log score zero.

This is a discrete HMM decoder, not a parameter estimator, continuous-observation model, conditional random field or map-matching system. Map matching additionally needs a defensible transition model, network topology, candidate generation and distance/time assumptions.
