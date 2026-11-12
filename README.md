# Spatial Analysis

**Understand the methods behind the maps, models and decisions that shape our world.**

Spatial data is everywhere. It helps us find places, plan journeys, understand changing environments, measure access to services and make better decisions about the places we share.

But what actually happens behind the map? How does a computer know two areas overlap? How do we find the best route, measure a pattern, predict what might change or decide where something should go?

This is a place to find out.

We explore the ideas behind spatial analysis, make them easier to understand, try them with real examples and show where they are useful. From the fundamentals to the methods used in research and production, the goal is simple: help more people understand what these tools do, when to use them and how to put them to work.

## What you can do here

- **Make sense of a method.** Clear explanations of what it does, how it works and what to watch out for.
- **See it in action.** Examples, code, maps, tests and practical experiments.
- **Go deeper.** Mathematics, performance, trade-offs and the details that matter when the easy example isn't enough.
- **Find your way through.** Follow a guided path, start with a problem you have, or explore whatever catches your interest.
- **Build with others.** Share a correction, ask a question, contribute an implementation or help improve an explanation.

You do not have to start at the beginning. You do not have to know everything before you join in.

## Explore

| If you're interested in… | Start here |
|---|---|
| The building blocks of GIS | [Core GIS and geometry](learning-paths/README.md#start-with-a-problem) |
| How spatial algorithms work | [Algorithm collection](algorithms/README.md) |
| Working examples and code | [Implementations](implementations/README.md) |
| Testing speed and accuracy | [Benchmarks](benchmarks/) |
| Learning at your own pace | [Learning paths](learning-paths/README.md) |
| Helping improve the project | [Contributing](CONTRIBUTING.md) |

## A growing collection, not a closed course

Spatial analysis is too broad to fit into one fixed syllabus. Some people want the foundations. Others arrive with a question about transport, satellite imagery, public health, ecology, cities or spatial data engineering.

So the collection keeps growing. Each method has a home of its own, and learning paths bring related methods together for different goals. New research, examples and contributions can improve the collection over time.

## Start anywhere. Keep going as far as you like.

You can read, try an example, follow a learning path or help us make something clearer. The material is built to be useful on its own and better together.

---

## About this repository

This is the public home for the project's explanations, research references, examples and collaborative work. It is maintained as a version-controlled technical resource so that corrections and improvements remain visible.

The initial scope comes from the supplied *Spatial Analysis Algorithms: Complete Compendium* (47 pages, 12 November 2026). Its page-by-page text is preserved under [source-inventory](source-inventory/README.md). The original inventory is broad and includes algorithms, operations, statistical models, data structures, software, metrics and applied methods. Each item is reviewed before being presented as established technical guidance.

### How the work is made

- [How we research and explain a method](docs/project-method.md)
- [How we write and teach](docs/voice-and-writing.md)
- [How we check technical claims](docs/research-standard.md)
- [How to contribute](CONTRIBUTING.md)
- [The writing and teaching principles](docs/voice-and-writing.md)
- [The learning and membership experience](docs/publishing-model.md)

### First example

Start with [polygon intersection](algorithms/geometry/polygon-intersection.md): how do we find the part shared by two shapes? Read the explanation, then [run the Python example](implementations/python/polygon-intersection/README.md) and its tests. The example is implemented with Shapely 2.1.2; the test suite has passed in the recorded environment.

A second foundational example is [point in polygon](algorithms/geometry/point-in-polygon.md): given a point and a boundary, is it inside, outside or on the edge? It includes a small ray-crossing implementation and 11 tests.

The weekly edition format is documented in the [newsletter issue template](docs/newsletter-issue-template.md).

**Current stage:** the source collection and project foundations are in place. We are now turning the inventory into clear explanations, working examples and useful ways to learn.
