# Licensing decision proposal

**Status: recommendation prepared; no project-wide licence has been applied.**

This proposal is here so the repository can become genuinely open to reuse and contribution without accidentally relicensing material that belongs to someone else.

It is not legal advice. If the repository is going to support commercial publishing, paid membership or institutional licensing, have the final arrangement reviewed by a qualified adviser.

## Why this decision matters

A public GitHub repository is not automatically open-licensed. Without a licence, copyright remains with the rights holder and other people generally do not receive permission to reuse, adapt or redistribute the material.

The repository needs separate decisions for:
- original source code;
- original explanations, tutorials and diagrams;
- third-party figures, text, code and datasets;
- the supplied 47-page compendium and its page transcriptions;
- contributions from future authors.

One licence should not be assumed to cover all of those materials.

## Recommended starting point

| Material | Recommendation | Why |
|---|---|---|
| Original code and tests | Apache License 2.0 | Permissive open-source licence with an express patent grant and clear contribution terms |
| Original lessons, tutorials and project-created diagrams | CC BY 4.0 | Allows sharing and adaptation, including commercial reuse, with attribution |
| Third-party figures and excerpts | Keep their original licence and attribution with each asset | The project cannot relicense material it does not own |
| Datasets | Record the dataset's own licence and terms | Dataset rights and access conditions vary |
| Supplied compendium and page transcriptions | Do not apply a new licence until ownership and redistribution rights are confirmed | User-provided material is not automatically available for public redistribution |

### Why Apache-2.0 for code?

Apache-2.0 is a permissive open-source licence and includes an express patent licence. It requires retaining licence and notice information when redistributing the work. The MIT licence is a simpler alternative, but it does not contain the same express patent grant.

Official text: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Why CC BY 4.0 for learning material?

CC BY 4.0 allows people to copy, redistribute and adapt the material, including commercially, provided they give appropriate credit, link to the licence and indicate changes. It does not force every adaptation to use the same licence.

CC BY-SA 4.0 is a valid alternative if the project wants adaptations to remain under the same or a compatible licence. That share-alike condition has consequences for material combined with or adapted from the work.

Official terms:
- [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

The NonCommercial licences should not be used for project-owned material if the intention is to reuse the material in paid editions, courses or institutional offerings. A non-commercial licence restricts commercial use.

## Third-party figures and diagrams

A figure being visible on a website does not mean it is free to copy.

Before embedding a third-party visual, record:
1. the creator or rights holder;
2. the original source page or file;
3. the exact licence and version;
4. the required attribution;
5. whether modifications were made;
6. the date the licence was checked.

Prefer public-domain material or licences that permit commercial reuse and adaptation, such as CC BY or CC BY-SA. Do not assume a website's software licence also covers every image on that website.

If permission is unclear, link to the original figure instead of copying it. The [visual sources and attribution register](visual-sources-and-attribution.md) records material already used.

## Contributions

Recommended approach:
- contributors retain copyright in their original contributions;
- contributions are submitted under the relevant project licence;
- use the Developer Certificate of Origin (DCO) sign-off in commit messages;
- do not require a contributor to assign copyright merely to fix a typo, add a test or suggest a source;
- do not accept code, text, images or data unless the contributor has the right to submit them under the stated terms.

A DCO records that a contributor is entitled to submit the contribution and agrees to the project's contribution terms. It does not replace the licence itself.

## The supplied compendium

The source inventory began with a 47-page compendium supplied in this conversation. The repository currently contains page-by-page text transcriptions and section indexes derived from that material.

Before adding a project-wide licence:
- confirm who created the compendium;
- confirm whether it includes copied or adapted third-party material;
- identify any source text, tables or figures that cannot be redistributed;
- decide whether the public repository should retain the full transcription, a citation-only index or a redacted version.

Until those rights are clear, do not represent the compendium or its transcriptions as CC BY, Apache-2.0 or any other project licence.

## Decisions to confirm before applying licences

1. **Code:** approve Apache-2.0, or choose MIT.
2. **Original learning material:** approve CC BY 4.0, or choose CC BY-SA 4.0.
3. **Compendium:** confirm ownership and redistribution rights for the supplied source and derived transcriptions.
4. **Contributions:** approve DCO sign-off for future contributions.
5. **Third-party material:** keep per-asset licensing and attribution records.

Once those decisions are confirmed, the repository can add the appropriate `LICENSE`, documentation licence notice, DCO instructions and any required `NOTICE` file. Do not add a blanket licence before those decisions are made.

## Current state

- No project-wide code licence has been applied.
- No project-wide documentation licence has been applied.
- Existing third-party figures retain their stated source licences and attributions.
- The source compendium's redistribution rights remain unconfirmed.
- The repository should not yet promise contributors that all content can be reused under one blanket licence.
