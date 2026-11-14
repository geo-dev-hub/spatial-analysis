# Intern walkthrough: diversity and multigroup segregation

For category counts n_i, proportions are p_i=n_i/sum(n). Shannon entropy is H=-sum(p_i log p_i), with zero-count categories contributing zero. Simpson concentration is D=sum(p_i²); Gini–Simpson diversity is 1-D. Higher Shannon entropy and lower Simpson concentration indicate greater diversity.

For a matrix x_ik of group k counts in areal unit i, the Reardon–Firebaugh multigroup entropy index is H_seg=(E-E_bar)/E. E is entropy of the overall group proportions; E_bar is the population-weighted mean of within-unit entropies. The index is zero when every unit has the same composition and one under complete separation, provided overall entropy is positive.

The exposure probability P*ij=sum_k (x_ik/X_i)(x_jk/t_k) is the probability that a randomly selected member of group i shares an areal unit with a member of group j under the index's population weighting. The diagonal gives isolation. This implementation does not weight by distance or adjacency; spatially explicit exposure requires a different neighbourhood model.
