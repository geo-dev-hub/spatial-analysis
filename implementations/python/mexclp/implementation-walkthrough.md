# Intern walkthrough: build a small MEXCLP solver

## 1. Translate the planning question

We need to place p service units so that as much weighted demand as possible has at least one available unit within a service threshold. A nearby unit is not guaranteed to be free.

## 2. Convert distance into eligibility

For every demand row i and candidate site j, test whether cost d_ij is less than or equal to the chosen threshold S. The resulting Boolean matrix records which candidate sites can reach each demand location.

Do not silently change cost units. A matrix of minutes and a threshold of kilometres are incompatible.

## 3. Count covering units

A placement is a sorted tuple of candidate indices. Repeated indices are allowed because multiple units can be based at one candidate site. For each demand row, count the selected unit placements whose sites are eligible.

## 4. Convert availability into expected coverage

If k units cover a demand row and each has busy probability q, the model assumes independent busy states. The probability that all k are busy is q^k, so the chance that at least one is available is 1 - q^k. Multiply by the row's demand weight.

A row with no covering units has k = 0 and contributes zero. With q = 0, any covered row contributes its full demand weight.

## 5. Search every small placement

The solver uses combinations with replacement. For m candidate sites and p units there are choose(m + p - 1, p) placements when p is positive. This makes the implementation easy to inspect and verify, but the count grows rapidly.

## 6. Keep tie behaviour reproducible

Placements are generated in lexicographic order. When expected coverage is equal, the first placement remains selected. This deterministic rule makes tests and notebook outputs repeatable; it is not a policy preference.

## 7. Validate the result

The tests check the one-unit formula, diminishing returns from a second cover, a case where units should be spread across sites, zero units, zero busy fraction, ties and invalid inputs. For a real planning study, compare the output with an independent solver on small cases and inspect the coverage matrix.

## 8. What not to claim

The solver does not estimate q, model correlated unit availability, queue waiting, service-time distributions, dispatch priority, finite station capacity or time-of-day variation. The equal independent busy-fraction assumptions are central to the MEXCLP approximation, not incidental implementation details.
