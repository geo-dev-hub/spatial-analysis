# Exercise: build confidence in a geometric predicate

## Scenario

A polygon overlay or triangulation routine occasionally fails on nearly collinear coordinates. You suspect that a floating-point orientation test is returning an unreliable sign.

## Part A — Establish the contract

1. Install the package requirements and run the tests.
2. Write three triples representing counter-clockwise, clockwise and collinear cases.
3. Evaluate the determinant by hand for one example.
4. Explain why the function returns a sign rather than a constructed coordinate.

## Part B — Explore numerical behaviour

1. Compare the exact rational predicate with the naive floating-point determinant on the near-degenerate fixture.
2. Scale and translate integer coordinates. Which transformations preserve the sign?
3. Swap two input points. What should happen?
4. Replace one coordinate with a non-finite value. Why should the function reject it?
5. Generate random integer triples and compare the exact predicate with a floating-point implementation. Record every disagreement.

## Part C — Design a production strategy

Write a short design note comparing:

- exact rational arithmetic for every input;
- a fast floating-point filter with a proven error bound and exact fallback;
- a fixed epsilon rule;
- a library geometry kernel with exact predicates.

Discuss correctness, performance, construction precision and the meaning of the original input coordinates.

## Deliverable

Submit the test script, a table of numerical disagreements and a one-page recommendation for the geometry kernel you would use in a production overlay or triangulation system. Do not describe the Fraction implementation as an adaptive Shewchuk predicate.
