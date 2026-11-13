# Build a learning experience, not just a page

A strong lesson helps someone move from a question they recognise to an idea they can explain, test and use. The repository has many tools available, but each one should earn its place by making a particular part of the method easier to understand.

Our guiding principle is **familiar on the surface, rigorous underneath**. Begin with the reader's question. Bring in technical language when it becomes useful. Keep the full mathematical and computational detail available for readers who want it.

## The learning sequence

A useful lesson usually moves through these stages:

1. **Recognise the question.** Start with a real task, decision or puzzle.
2. **Get the idea.** Explain the central concept without requiring prior specialist vocabulary.
3. **See it.** Use the clearest visual representation of the relationship or process.
4. **Understand the machinery.** Introduce definitions, equations, assumptions and algorithm steps.
5. **Try it.** Let the reader predict an answer, run an example or change an input.
6. **Check the result.** Use tests, expected outputs, invariants or a reference implementation.
7. **Know the limits.** Explain edge cases, uncertainty, failure modes and trade-offs.
8. **Go further.** Link to a related method, a learning path, source material or a research question.

Not every topic needs eight large sections. Keep the sequence, but let the method determine the depth.

## Choose the right tool

| If the reader needs to… | Use… | Make sure… |
|---|---|---|
| Understand a geometric relationship | Reused licensed figure or original SVG | Coordinates, labels and boundary cases are clear |
| Follow a process or decision | Mermaid flowchart | Each branch represents a real decision or state |
| Understand an event sequence | Sequence diagram, timeline or animation | The order and changing state are accurate |
| Understand a formula | Rendered Markdown mathematics | Symbols, assumptions and meaning are explained |
| See where something happens | Map with a small, documented dataset | CRS, scale, attribution and data licence are stated |
| Understand a numerical pattern | Reproducible plot | The data, axes, units and code are available |
| Explore how inputs change an answer | Notebook or interactive demonstration | Controls expose meaningful parameters, not decorative effects |
| Learn how code works | Runnable example and annotated walkthrough | The environment, expected output and limitations are explicit |
| Build confidence | Tests and worked examples | Tests cover meaningful cases, including failure cases |
| Compare performance | Reproducible benchmark | Workload, hardware, versions and measurement method are recorded |
| Practise independently | Exercises with hints and checks | The task is clear and does not depend on hidden setup |

Use more than one format when the combination helps. For example, an SVG can explain the geometry, a notebook can let the reader move a point, and a test can verify the boundary case. Avoid repeating the same information in several formats without a learning reason.

## Diagrams and external figures

A diagram is useful when it reveals something that prose alone makes difficult to see: spatial relationships, data structures, geometric cases, event order, state transitions or the effect of a parameter.

Before drawing a new one:

1. Search for the original paper, official documentation, university course or research group material.
2. Inspect the exact figure and its file-level rights.
3. Reuse it only when the licence or written permission covers our intended public and potentially commercial use.
4. Preserve attribution and licence notices, and disclose any changes.
5. If permission is unclear, link to the original and identify the relevant figure or page.
6. Draw an original figure only when it adds clarity, a new example or a view the source does not provide.

A citation is not permission. A licence on a paper or slide deck may not cover a separately credited figure. Keep the source record in [the visual-source register](visual-sources-and-attribution.md).

## Mathematics should be readable

Use GitHub's rendered Markdown mathematics rather than pasted equation images. Use inline notation for short expressions and display equations for important definitions, derivations or results.

Every equation should answer a question. Define symbols near their first appearance, state the assumptions and translate the expression into ordinary language. Where a result depends on a convention—such as a null model, coordinate system, boundary rule or weight transformation—say so.

Follow [the mathematics and visuals guide](math-and-visuals.md), and preview formulas in GitHub's rendered view before treating a lesson as ready.

## Make interactive material worth opening

A notebook or interactive example should give the reader something they cannot get as easily from a static paragraph. Good interactions include:

- moving a query point and seeing a point-in-polygon classification change;
- changing polygon positions and inspecting intersection geometry;
- adding segments and watching sweep events appear in order;
- changing a spatial weights definition and comparing the resulting statistic;
- changing index node capacity and seeing candidate counts change;
- varying sample size or spatial pattern and inspecting a plot.

Keep the default example small and understandable. Explain what each control changes. Include a reproducible static result so the lesson still makes sense when the notebook cannot be run.

## Accessibility and reliability

- Give every meaningful image useful alt text or a descriptive caption.
- Do not communicate a result through colour alone; use labels, symbols or line styles too.
- Label chart axes and include units.
- Keep notebook setup instructions short and tested.
- Avoid oversized datasets and unnecessary dependencies.
- Provide expected outputs and tests for code examples.
- Make sure a lesson remains understandable on a phone-sized screen.
- Keep the written explanation available; do not make a visual or interactive widget the only place where essential information appears.

## When is a lesson ready?

A lesson is ready for wider publication when a reader can answer:

- What question does this method help me answer?
- What goes in, and what comes out?
- What is the simple idea?
- What are the formal definition and assumptions?
- How does the method work?
- Can I follow a worked example?
- Can I run or inspect a meaningful demonstration?
- How do we know the result is correct?
- What can go wrong?
- Where can I go next?

Technical review, licence review and rendered-page checks are still required. A polished presentation does not substitute for evidence.
