# Reusing diagrams, figures and other visual sources

A good technical explanation should use the best visual evidence available. We should not redraw an accurate source figure merely to make it look like our own. When a relevant diagram already exists, first check whether we can reuse it.

## Our rule

1. **Find the strongest original source.** Prefer the paper, author, research group, university course or official technical documentation over reposts and unattributed copies.
2. **Check the exact asset's rights.** A public PDF or webpage is not automatically licensed for redistribution. A citation is not a licence.
3. **Reuse when permission is clear.** Public-domain works and licences that permit our intended use may be reproduced with the required attribution and licence notice. Check whether commercial use, adaptations and redistribution are permitted; our material may be published publicly and may later support paid learning.
4. **If rights are unclear, link to the original.** Describe which figure, slide or page is useful and why. Do not download, crop, screenshot, embed or commit a copy unless a permitted basis is established.
5. **Create an original visual when it adds value.** Use our own diagram to explain a specific step, annotate a subtle point, show a different example, or connect the source's ideas to our implementation. Label it as project-created.
6. **Record the provenance.** For every reused visual, record creator, title, source URL, figure/page number, licence and version, required attribution, modifications made, and the date rights were checked.

## What counts as sufficient permission?

Good evidence includes an explicit Creative Commons or other reuse licence attached to the work, a public-domain statement, or written permission from the rights holder. The licence must cover our actual use. For example, a non-commercial-only licence is not suitable for material that will be incorporated into a commercial product or paid publication.

When a figure is contained in a paper, book or lecture deck, check whether it is the author's own work or is credited to a third party. The overall document's licence may not cover a separately credited figure.

## Attribution format

Place a credit immediately below the visual, with a fuller entry in the references or visual-source register.

Suggested format:

> **Source:** [Creator], “[Work title],” Fig. [number] / p. [page], [year], [source link]. [Licence and link]. [Changes: none / cropped / adapted / translated].

For adapted figures, say “Adapted from” and briefly describe the changes. Never imply that the original author or institution endorses this project.

## Link instead of copying

Linking readers to a lawfully hosted original is a useful teaching practice when redistribution rights are not clear. Include a short note about the relevant slide or page so the reader knows what to look for.

## Current Bentley–Ottmann example

The algorithm record links to Laura Toma's Bowdoin lecture slides and Pat Morin's Carleton lecture notes because both contain valuable event-by-event diagrams. We have not found an explicit open reuse licence for those figures in the materials checked, so we link to the original PDFs rather than copying their images. The repository's separate sweep illustration is an original project-created schematic.

## Visual-source register

The following sources have been checked for the specific figure used in the linked lesson:

| Lesson | Figure and creator | Source | Licence | How it is used |
|---|---|---|---|---|
| [Point in polygon](../algorithms/geometry/point-in-polygon.md) | “Point in polygon problem,” Adam Majewski | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Point_in_polygon_problem.svg) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Embedded unchanged from the original Wikimedia-hosted SVG; attribution is placed below the image |
| [Polygon intersection](../algorithms/geometry/polygon-intersection.md) | “Vector Overlay Operators,” Bplewe | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Vector_Overlay_Operators.png) | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Embedded unchanged; the caption directs readers to the “intersect” row |
| [Bentley–Ottmann](../algorithms/geometry/bentley-ottmann.md) | “Segments intersections,” Sergey539 | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Segments_intersections.gif) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) or GFDL 1.2+ | Embedded unchanged as an animated overview; caption identifies the selected licence |
| [Segment intersection](../algorithms/geometry/segment-intersection.md) | “Is-linesegm.png,” Ag2gaeh | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Is-linesegm.png) | CC BY-SA 3.0, as stated on the file page | Link only; the direct image asset URL was not confirmed, so it is not embedded |

Both licences permit sharing and commercial use with attribution and share-alike obligations. The figures are embedded from their original Wikimedia Commons hosts, not copied into this repository. If we later download, modify, package or redistribute either asset, re-check the file page and preserve the licence requirements for that specific use.

For [segment intersection](../algorithms/geometry/segment-intersection.md), the [UPC Computational Geometry orientation-test lecture PDF](https://dccg.upc.edu/wp-content/uploads/2021/09/GeoC-Orientation-tests-R.pdf) contains useful diagrams for point-line orientation and segment crossing. We have not verified a reuse licence for those slides, so the repository links to the source rather than embedding or copying its figures.

## Before publishing a visual

- [ ] Is this the original or authoritative source?
- [ ] Have we checked the rights for this specific figure, not just the webpage?
- [ ] Does the licence permit redistribution and the intended commercial context?
- [ ] Have we preserved the required attribution and licence link?
- [ ] Have we disclosed cropping, recolouring, translation or other adaptations?
- [ ] Is the figure legible and explained in the surrounding text?
- [ ] If rights are unclear, have we linked to the original instead of copying it?
