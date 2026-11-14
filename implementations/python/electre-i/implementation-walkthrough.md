# Intern walkthrough: constructing an ELECTRE I-style relation

## Goal

Compare discrete alternatives pairwise. For each ordered pair, measure the weight of criteria supporting the assertion that a is at least as good as b, then check whether any criterion strongly opposes it.

This package implements the outranking relation only. It does not produce the final ELECTRE I kernel or a complete decision recommendation.

## 1. Prepare the decision matrix

Rows are alternatives; columns are criteria. Record the unit and meaning of each criterion before modelling. Mark each criterion as a benefit (larger is better) or a cost (smaller is better).

Weights represent the relative importance of criteria in the concordance coalition. They are normalised to sum to one by the implementation. They are not data-quality scores.

## 2. Calculate concordance

For alternatives a and b, a criterion supports a outranking b when a is at least as good as b on that criterion. Add the normalised weights of all supporting criteria.

The result lies between zero and one. A higher value means a larger weighted coalition supports the assertion.

## 3. Calculate discordance

For each criterion where b performs better than a, divide b's advantage by the observed range of that criterion across all alternatives. The discordance index is the maximum of these ratios.

If a is no worse than b on every criterion, discordance is zero. A value near one means b has a very large advantage on at least one criterion relative to the observed range.

This is a documented range-normalised teaching convention. Other ELECTRE variants use explicit indifference, preference and veto thresholds.

## 4. Apply the crisp outranking rule

The pair (a,b) is accepted when:

- concordance(a,b) is at least the concordance threshold; and
- discordance(a,b) is at most the discordance threshold.

Both thresholds are decision parameters. Explore plausible values and report how the relation changes.

## 5. Read the output as a relation, not a ranking

The output matrix has rows as potential outrankers and columns as alternatives being compared. A True entry at [a,b] means a outranks b under the specified rule.

The relation can contain cycles or incomparable pairs. Do not force it into a total ranking without an explicit, justified exploitation procedure. A full ELECTRE I choice analysis also requires a kernel procedure; this package does not implement that step.

## 6. Tests to study

Tests cover benefit/cost orientation, weight normalisation, pairwise ties, reflexivity, incomparability, constant criteria and invalid input contracts.

## 7. Extension exercise

Change the concordance and discordance thresholds. Identify an alternative pair whose relation changes. Explain which coalition supports the pair and which criterion supplies the strongest opposition.

Then design a small spatial decision involving three candidate service sites. Include at least one benefit criterion (accessibility) and one cost criterion (travel cost or hazard exposure). Explain why the result is not a continuous suitability map.


## 8. Extract and interpret the kernel

The companion `electre_i_kernel.py` module takes the Boolean outranking matrix and checks two conditions for each candidate subset:

- **Internal stability:** no two distinct selected alternatives outrank one another.
- **External stability:** each alternative outside the subset is directly outranked by at least one selected alternative.

The output is a set of one or more kernels. An empty result means no subset satisfies both conditions for the supplied relation. Multiple results mean the relation does not identify a unique kernel. The implementation deliberately reports these cases rather than applying an undocumented cycle-reduction rule.

The implementation checks direct edges, not transitive reachability. If A outranks B and B outranks C, that does not by itself mean A directly outranks C for the external-stability test.

The search enumerates subsets and is exponential. It is capped at 20 alternatives by default and is intended for small decision problems. The kernel is a choice set, not a total ranking. Inspect cycles, thresholds and criterion assumptions before interpreting the result.
