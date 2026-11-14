# Hidden Markov models and Viterbi decoding for spatial sequences

A hidden Markov model (HMM) represents a sequence of latent states that generate observable symbols. In spatial work, the hidden state might be a road segment, land-cover class or movement mode; observations might be GPS positions, spectral classes or sensor events. The model is only as credible as its state space, transition assumptions, emission model and observation process.

## Model definition

For states \(S=\{s_1,\ldots,s_N\}\), observation symbols \(V=\{v_1,\ldots,v_M\}\), and observations \(O=(o_1,\ldots,o_T)\), a discrete HMM is specified by:

- initial state probabilities \(\pi_i=P(q_1=s_i)\);
- transition probabilities \(a_{ij}=P(q_{t+1}=s_j\mid q_t=s_i)\);
- emission probabilities \(b_j(v_k)=P(o_t=v_k\mid q_t=s_j)\).

Each probability vector or matrix row sums to one. The first-order Markov assumption says the next hidden state depends on the current state, not the full history; the emission assumption says the current observation depends on the current hidden state.

## Viterbi decoding

The decoding task is to find the single most probable hidden-state path given the observations and fixed model parameters. Define the best partial path score ending in state \(s_j\) at time \(t\):

$$
\delta_t(j)=\max_{q_1,\ldots,q_{t-1}}P(q_1,\ldots,q_t=s_j,o_1,\ldots,o_t\mid\lambda).
$$

Initialisation:

$$
\delta_1(j)=\pi_j b_j(o_1).
$$

Recurrence:

$$
\delta_t(j)=b_j(o_t)\max_i\left[\delta_{t-1}(i)a_{ij}\right].
$$

Store the predecessor that achieves each maximum. Select the best final state, then backtrack through those predecessor pointers. In implementation, use log probabilities:

$$
\ell_t(j)=\log b_j(o_t)+\max_i\left[\ell_{t-1}(i)+\log a_{ij}\right].
$$

This converts products into sums and avoids underflow. A zero probability maps to \(-\infty\); if every path has zero probability, decoding should fail explicitly.

## What the decoder returns—and what it does not

The Viterbi path is the single best *joint sequence*. It is not necessarily the sequence obtained by choosing the most probable state independently at each time. It does not estimate the transition or emission parameters; parameter estimation (for example Baum–Welch/EM) is a separate task. Nor does a discrete HMM automatically solve map matching: candidate states, network connectivity, distance/time emissions, sampling gaps and transition penalties must be designed for the application.

## Runnable implementation

The [Python teaching package](../implementations/python/hmm-viterbi/README.md) implements a discrete-emission Viterbi decoder with log-space arithmetic, explicit state and symbol order, probability validation, zero-probability handling and deterministic tie-breaking. It includes [tests](../implementations/python/hmm-viterbi/test_hmm_viterbi.py), an [intern walkthrough](../implementations/python/hmm-viterbi/implementation-walkthrough.md) and an [executable lab notebook](../notebooks/hmm-viterbi-lab.ipynb). It does not estimate HMM parameters or implement continuous emissions or map matching.

## Tests and experiments

- Compare the decoded sequence with a hand-enumerated tiny model.
- Verify that zero-probability transitions and emissions behave as impossible paths.
- Check empty sequences, unknown symbols, malformed probability tables and matrix dimensions.
- Construct a tie and verify the documented state-order tie break.
- For spatial applications, vary transition and emission assumptions and evaluate against held-out trajectories or labelled sequences—not just training likelihood.

## Reference

Rabiner, L. R. (1989), “A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition,” *Proceedings of the IEEE*, 77(2), 257–286. [DOI: 10.1109/5.18626](https://doi.org/10.1109/5.18626). The paper describes the three classical HMM problems and the Viterbi dynamic-programming recurrence.
