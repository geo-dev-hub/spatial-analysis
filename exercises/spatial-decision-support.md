# Spatial decision-support exercises

These exercises use the [weighted linear combination lesson](../methods/weighted-linear-combination.md) and its [interactive lab](../notebooks/weighted-linear-combination-lab.ipynb). The aim is to test the decision model, not just reproduce the weighted-sum arithmetic.

## 1. State the decision

Choose a hypothetical decision such as identifying candidate areas for a community facility.

- Define the objective and the alternatives.
- Identify who benefits and who may bear costs.
- List at least three factors and two hard constraints.
- State the spatial unit, time period and coordinate/data requirements.
- Explain what evidence could validate the result.

Do not treat an available data layer as a criterion until you can explain why it is relevant to the decision.

## 2. Standardise two criteria in opposite directions

Create a raw distance layer and a raw slope layer.

- Transform distance so that closer locations receive higher preference.
- Transform slope so that the preferred terrain receives higher preference.
- Compare linear scaling with a nonlinear value function.
- Identify the effect of the minimum and maximum values on every score.
- Explain what happens when a criterion is constant.

## 3. Separate factors from constraints

Create a protected-area mask and a flood-risk factor.

- Exclude protected cells with a Boolean mask.
- Keep flood risk as a factor only if the decision permits trade-offs.
- Compare the result with a model that treats a flood threshold as a hard exclusion.
- Explain why a very low score is not equivalent to a hard exclusion.

## 4. Challenge the weights

Start with three weights that sum to one.

- Increase one weight while proportionally reducing the others.
- Compare the highest-ranked locations.
- Find the smallest weight change that changes the top-ranked cell.
- Explain which decisions are robust and which are sensitive.
- Ask whose preferences the weights represent.

## 5. Look for double-counting

Identify two criteria that may represent the same underlying factor, such as road distance and travel time to a road-accessible service.

- Compare their correlation.
- Run a model with both criteria and a model with only one.
- Explain whether the two layers contribute independent information.
- Do not remove a criterion solely because it is correlated; justify the modelling decision.

## 6. Validate and communicate

- Compare high-scoring locations with independent evidence or known examples.
- Inspect locations that the model ranks highly but domain experts consider unsuitable.
- State the model's limitations, assumptions and uncertainty.
- Present at least two plausible scenarios rather than one definitive suitability map.
- Explain why the score is not a probability or an objective statement of truth.

## Submission checklist

- [ ] Decision objective and affected groups are explicit.
- [ ] Factors and constraints are separated.
- [ ] Standardisation functions and directions are documented.
- [ ] Weights have a stated source and rationale.
- [ ] Grid alignment, units and NoData rules are documented.
- [ ] Sensitivity analysis is included.
- [ ] Validation evidence and unresolved limitations are stated.
