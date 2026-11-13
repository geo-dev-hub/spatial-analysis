# ELECTRE: outranking when trade-offs should not be automatic

ELECTRE is a family of multi-criteria decision-aiding methods built around pairwise outranking relations. It is not one single algorithm. ELECTRE I, II, III, IV and TRI address different problem types and use different preference information and exploitation procedures.

The central question is not simply “Which alternative has the highest total score?” It is closer to: **Is there sufficient support to say that alternative a is at least as good as alternative b, without a decisive objection on some criterion?**

## Concordance and discordance

For a pair of alternatives (a,b), concordance measures the coalition of criteria that supports the claim that a outranks b. In a simple weighted form:

\[
C(a,b)=\sum_{j\in J(a,b)}w_j,
\]

where J(a,b) is the set of criteria on which a is judged at least as good as b, and the non-negative weights express criterion importance.

Discordance captures strong opposition: a criterion on which b is much better than a may act as a veto or block the outranking claim. More advanced ELECTRE variants use indifference, preference and veto thresholds to represent imperfect measurement and meaningful differences.

A simplified crisp outranking rule might require both:

\[
C(a,b)\geq c^*,\qquad D(a,b)\leq d^*.
\]

This is only a teaching sketch. ELECTRE III, for example, uses richer partial concordance and credibility calculations; do not substitute the simple rule for a named variant.

## Why choose outranking?

ELECTRE can be useful when:
- alternatives are discrete and explicitly enumerated;
- criteria use different units or are not naturally commensurable;
- decision-makers do not want every weakness to be compensated by strengths elsewhere;
- thresholds can express indifference, meaningful preference and unacceptable disadvantage;
- a partial order or shortlist is more honest than forcing a complete ranking.

Outranking relations may be incomplete or non-transitive. A method can leave alternatives incomparable. That is not necessarily a software defect; it can be a faithful expression of conflicting criteria and limited preference information.

## How it differs from other Section 7 methods

| Method | Main question | Output form | Compensation |
|---|---|---|---|
| WLC | What weighted score does each location receive? | Continuous composite score | Yes |
| OWA | How should the best-to-worst ordered values be combined? | Aggregated score | Depends on order weights |
| TOPSIS | Which alternative is closest to ideal and farthest from anti-ideal? | Relative closeness ranking | Yes |
| ELECTRE | Is there enough support to outrank another alternative without a decisive veto? | Outranking relation, then choice/ranking/sorting | No systematic compensation |

## Spatial decision workflow

1. Define the alternatives. ELECTRE is generally more natural for candidate sites, plans or scenarios than for producing a continuous suitability surface over every raster cell.
2. Specify criterion directions, units, weights and data quality.
3. Elicit indifference, preference and (where relevant) veto thresholds with domain experts.
4. Select the ELECTRE variant that matches the task: choice, ranking or sorting.
5. Calculate pairwise concordance and discordance/credibility according to that variant.
6. Inspect the resulting outranking graph or relation, including cycles and incomparable pairs.
7. Explore how conclusions change when thresholds and weights vary.
8. Explain why an alternative is or is not outranked; do not hide the result behind a single opaque score.

## Implementation status

This repository currently provides a researched conceptual lesson, not a tested ELECTRE implementation. The family is too broad to represent responsibly with a few lines of generic concordance code. A future implementation must name its variant, threshold semantics, exploitation procedure and validation examples. Do not label a simplified crisp concordance/discordance screen as “ELECTRE” without qualification.

## References

- Roy, B. (1968). Classement et choix en présence de points de vue multiples (la méthode ELECTRE). Revue française d'informatique et de recherche opérationnelle, 2(V8), 57–75.
- Figueira, J. R., Greco, S., Roy, B. & Słowiński, R. (2013). An Overview of ELECTRE Methods and their Recent Extensions. Journal of Multi-Criteria Decision Analysis, 20, 61–85. https://doi.org/10.1002/mcda.1482
- Govindan, K. & Jepsen, M. B. (2016). ELECTRE: A comprehensive literature review on methodologies and applications. European Journal of Operational Research, 250(1), 1–29. https://doi.org/10.1016/j.ejor.2015.07.019
- UK Department for Communities and Local Government (2009). Multi-criteria analysis: a manual, Section 6.

This is a method-family overview. Choose and document a specific ELECTRE variant before applying it.
