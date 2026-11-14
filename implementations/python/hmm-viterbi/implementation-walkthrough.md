# Viterbi decoder walkthrough

1. Validate the state and symbol alphabets and confirm each probability row sums to one.
2. Convert probabilities to log probabilities. Products become sums and zero probabilities become negative infinity, avoiding numerical underflow.
3. Initialise each state's score with the log start probability plus the first observation's emission log probability.
4. For each later observation and destination state, select the predecessor maximising previous score plus transition log probability; add the destination state's emission score.
5. Store predecessor indices, choose the best final state and backtrack to recover the complete state path.
6. Test known sequences, impossible observations, empty sequences, invalid probability tables and deterministic tie-breaking.
