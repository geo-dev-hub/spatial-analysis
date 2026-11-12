# Help make spatial analysis easier to understand

You don't have to be an expert to make this collection better.

Maybe you spotted an error. Maybe you know a useful paper, found an edge case, built a small example or have a question that the explanation didn't answer. Those are all good reasons to get involved.

## You can help by…

- suggesting a method or topic we have missed;
- asking a question or pointing out something that isn't clear;
- sharing a paper, documentation page or other useful reference;
- correcting an explanation or adding an example;
- contributing code, tests, notebooks or visualisations;
- trying an exercise and telling us where you got stuck;
- sharing a dataset or benchmark result that others can reproduce;
- translating or improving learning materials.

Small contributions matter. A clear issue report can be just as useful as a large code change.

## Before you send a change

1. Check whether the topic or issue is already in the collection.
2. Tell us what you changed and why.
3. Include a source for technical claims.
4. If you share code, include the versions and steps needed to run it.
5. For spatial examples, state the coordinate reference system, units and any important assumptions.
6. Only share data, code and images that you have permission to redistribute.

If you're unsure how to contribute, open an issue and describe what you have in mind. GitHub offers short forms for technical corrections, topic suggestions and visual sources. You can start a conversation before preparing a full change.

If you are ready to make a change, open a pull request. The repository checklist will help reviewers check the evidence, tests, mathematics, visuals and reuse rights.

### Run the checks

From the repository root, run the checks relevant to your change:

```bash
# Check relative links in Markdown files and notebook Markdown cells
python scripts/check_internal_links.py

# Run one Python example's test suite
cd implementations/python/geary-c
python -m pip install -r requirements.txt
python -m pytest -q
```

The GitHub Actions workflow runs all six Python example suites and executes all six notebooks. It also checks local links on relevant changes. If you change a notebook, run it from top to bottom before opening the pull request; a successful CI run is useful evidence, not a substitute for checking the explanation and assumptions.

## Help us keep it trustworthy

We want explanations that are approachable without being careless.

- Tell readers when a method is exact, approximate, heuristic or stochastic.
- Separate what the mathematics guarantees from what a particular software package does.
- Explain when a result depends on the data, coordinate system, precision or software version.
- Don't present one benchmark as proof that a method is always faster.
- Never invent a source, result or test.

## Credit and reuse

Read the [licensing and reuse note](docs/licensing-and-reuse.md) before contributing material that will be redistributed. The project has not selected blanket licences for code or documentation yet, and the supplied source inventory is not automatically covered by a future project licence.

Substantial contributions will be credited in the relevant material or project notes. Please link to original sources rather than copying large sections of someone else's writing, figures, code or datasets.

The project will publish clear licences for code and documentation. Until those are in place, please ask before assuming a contribution can be reused elsewhere.

## What happens next?

Contributions may be reviewed for accuracy, clarity, accessibility and reproducibility. We may suggest changes or ask a follow-up question. When people disagree about a technical detail, we'll make the assumptions visible and use evidence to work through it.

Thanks for helping make spatial analysis clearer, more useful and easier to explore.
