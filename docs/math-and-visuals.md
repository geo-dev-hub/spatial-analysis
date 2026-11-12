# Make the ideas visible

A reader should not have to imagine every geometric relationship or decode a formula from plain text. Use the format that makes the idea easiest to understand, while keeping the source and reasoning available.

## Mathematical notation

GitHub renders mathematical expressions in Markdown. Use:

- inline mathematics for short expressions: `$A \cap B$`;
- display mathematics for equations that deserve their own line: `$$ ... $$`.

Example:

$$
A \cap B = \{x \mid x \in A \text{ and } x \in B\}
$$

The expression says that the intersection contains exactly the points that belong to both sets.

### Formula checklist

- Define every symbol close to where it first appears.
- State the assumptions behind the expression.
- Explain the equation in ordinary language.
- Use consistent notation throughout a page.
- Use `\text{...}` for words inside an equation.
- Use `\operatorname{...}` for named mathematical operators where appropriate.
- Avoid screenshots of equations when selectable, rendered mathematics is possible.
- Preview the page on GitHub before publication; do not assume every Markdown renderer behaves identically.

A formula is not decoration. If it does not help the reader understand, derive, test or use the method, explain why it is there.

## Diagrams and figures

Choose the visual form that fits the job:

| Need | Preferred format | Why |
|---|---|---|
| Geometry, topology, spatial relationships | SVG | Precise coordinates, labels and scalable rendering |
| Algorithm flow or decision logic | Mermaid | Editable text and easy maintenance |
| Event sequence or data-structure state | Mermaid or SVG | Shows order and state changes |
| Real-world spatial pattern | Map or geospatial dataset | Preserves geographic context |
| Numerical behaviour | Plot generated from code | Reproducible and tied to data |
| Detailed exploration | Notebook or runnable demo | Lets readers change inputs and inspect results |

Use a source figure when it is the clearest explanation and its reuse rights permit the intended publication. Otherwise link to the original and identify the useful figure, slide or page. Attribution does not replace permission.

### Visual checklist

- The figure answers a specific question.
- Labels, symbols and units are readable.
- The surrounding text explains what to notice.
- The caption says whether the figure is original, reused or adapted.
- Alt text communicates the important information without relying on colour alone.
- The source and exact licence are recorded.
- Any adaptation is disclosed.
- The visual is checked at normal reading size and on a narrow screen.

## Runnable visual learning

A diagram is often the first step, not the whole experience. Where it materially improves understanding, pair it with one or more of:

- a small dataset readers can inspect;
- a Python example or notebook;
- a step-by-step trace;
- a test that captures an edge case;
- a plot or map generated from the example;
- a benchmark that compares a clearly defined workload.

Keep examples small enough to follow. Link to the full implementation for readers who want to explore further.

## Source and licence record

For every reused visual, keep the creator, title, original URL, figure/page number, licence, licence URL, access date, required attribution and modifications in the visual-source register. Check whether the source contains third-party material that is excluded from the document's general licence.

See [Reusing diagrams, figures and other visual sources](visual-sources-and-attribution.md).
