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
| Testing speed and accuracy | [Benchmarks](benchmarks/README.md) |
| Practising with exercises | [Exercises](exercises/README.md) |
| Following research questions | [Research notes](research/README.md) |
| Exploring calculations interactively | [Notebooks and labs](notebooks/README.md) |
| Checking the source coverage | [Coverage matrix](catalog/coverage-matrix.md) |
| Learning at your own pace | [Learning paths](learning-paths/README.md) |
| Finding patterns in spatial data | [Spatial autocorrelation and hotspots](learning-paths/global-spatial-autocorrelation.md), [point-pattern analysis](learning-paths/point-pattern-foundations.md) and [spatial clustering](learning-paths/spatial-clustering-foundations.md) |
| Estimating values between observations | [Spatial interpolation foundations](learning-paths/geostatistics-foundations.md) |
| Working with raster distances | [Raster distance foundations](learning-paths/raster-distance-foundations.md) |
| Summarising raster neighbourhoods | [Focal raster statistics](algorithms/raster/focal-statistics.md) |
| Understanding how terrain drains | [Raster hydrology foundations](learning-paths/raster-hydrology-foundations.md) |
| Resampling raster data | [Nearest neighbour and bilinear interpolation](algorithms/raster/resampling.md) |
| Summarizing raster values by zone | [Zonal statistics](algorithms/raster/zonal-statistics.md) |
| Labeling connected raster regions | [Connected-component labeling](algorithms/raster/connected-components.md) |
| Learning geospatial self-supervision | [Contrastive learning with NT-Xent](algorithms/geoai/contrastive-info-nce.md) |
| Understanding coordinate reference systems | [Coordinate transformation](algorithms/geodesy/crs-transformation.md) |
| Interpreting satellite vegetation bands | [Remote sensing index foundations](learning-paths/remote-sensing-indices.md) |
| Choosing locations for services | [Location science foundations](learning-paths/location-science-foundations.md) |
| Combining spatial criteria for a decision | [Spatial decision support](learning-paths/spatial-decision-support.md), [weighted linear combination](methods/weighted-linear-combination.md) and [weights of evidence](methods/weights-of-evidence.md) |
| Searching large collections of features | [Spatial indexing](learning-paths/spatial-indexing.md) |
| Joining spatial layers | [Filter-and-refine spatial join](algorithms/query-processing/filter-refine-spatial-join.md) |
| Defining spatial neighbours | [Spatial weights matrix](methods/spatial-weights-matrix.md) |
| Helping improve the project | [Contributing](CONTRIBUTING.md) |

## A growing collection, not a closed course

Spatial analysis is too broad to fit into one fixed syllabus. Some people want the foundations. Others arrive with a question about transport, satellite imagery, public health, ecology, cities or spatial data engineering.

So the collection keeps growing. Each method has a home of its own, and learning paths bring related methods together for different goals. New research, examples and contributions can improve the collection over time.

## Start anywhere. Keep going as far as you like.

You can read, try an example, follow a learning path or help us make something clearer. The material is built to be useful on its own and better together.

---

## About this repository

This is the public home for the project's explanations, research references, examples and collaborative work. It is maintained as a version-controlled technical resource so that corrections and improvements remain visible.

The initial scope comes from the supplied *Spatial Analysis Algorithms: Complete Compendium* (47 pages, 12 November 2026). Its page-by-page text is preserved under [source-inventory](source-inventory/README.md). The original inventory is broad and includes algorithms, operations, statistical models, data structures, software, metrics and applied methods. Each item is reviewed before being presented as established technical guidance. All 22 original sections now have item-level intake indexes; these preserve the source groupings and mark what still needs verification. An indexed entry is not automatically a researched or validated lesson.

### How the work is made

- [How we research and explain a method](docs/project-method.md)
- [How we write and teach](docs/voice-and-writing.md)
- [How we reuse and attribute visual sources](docs/visual-sources-and-attribution.md)
- [How we check technical claims](docs/research-standard.md)
- [How to contribute](CONTRIBUTING.md)
- [How we use mathematics and visuals](docs/math-and-visuals.md)
- [How we choose learning tools and build an effective lesson](docs/learning-experience-standard.md)
- [How the catalogue distinguishes algorithms, operations, models and other record types](catalog/record-types.md)
- [What the source compendium covers](catalog/coverage-matrix.md)
- [Repository roadmap](docs/repository-roadmap.md)
- [Licensing and reuse](docs/licensing-and-reuse.md)
- [Research notes](research/README.md)
- [Exercises](exercises/README.md)
- [Benchmarks](benchmarks/README.md)
- [The learning and membership experience](docs/publishing-model.md)

### First examples

Start with [polygon intersection](algorithms/geometry/polygon-intersection.md): how do we find the part shared by two shapes? Read the explanation, then [run the Python example](implementations/python/polygon-intersection/README.md) and its tests. The example is implemented with Shapely 2.1.2; the test suite has passed in the recorded environment.

A second foundational example is [point in polygon](algorithms/geometry/point-in-polygon.md): given a point and a boundary, is it inside, outside or on the edge? It includes a small ray-crossing implementation and 12 tests.

A third is [segment intersection](algorithms/geometry/segment-intersection.md): do two lines cross, touch or overlap? Its pairwise Python implementation uses exact integer orientation tests and rational coordinates, with 11 tests.

Try the [interactive geometry foundations lab](notebooks/geometry-foundations-lab.ipynb) to move a point, adjust a segment and explore polygon overlays.

Go further with [Bentley–Ottmann](algorithms/geometry/bentley-ottmann.md), which finds intersections across a whole set of segments using a sweep line. The guide includes a sweep diagram, event-processing flowchart, rendered equations and an explicit account of the classical algorithm's assumptions. You can also [run the restricted Python teaching implementation](implementations/python/bentley-ottmann/README.md) and follow its [step-by-step walkthrough](implementations/python/bentley-ottmann/implementation-walkthrough.md); its nine tests compare results with the pairwise method.

## A first look at spatial patterns

Start with the [spatial autocorrelation learning path](learning-paths/global-spatial-autocorrelation.md). It connects six methods, from global Moran's I and Geary's C to local clusters, neighbourhood differences and Getis-Ord hotspots. Local Geary and global Getis-Ord G are supplementary companions added during research. For point data, the new [DBSCAN clustering lesson](algorithms/statistics/dbscan.md) shows how core points, border points and noise are distinguished.

You can read the individual lessons or open their [interactive notebooks](notebooks/README.md). The examples use small, reproducible data so you can change the values, inspect the spatial relationships and see what changes in the result.

The [algorithm collection](algorithms/README.md) also includes the foundational geometry lessons, [coverage-aware polygon simplification](algorithms/geometry/coverage-simplification.md), [precision models and snap rounding](algorithms/geometry/precision-models.md), an [STR-packed R-tree](algorithms/indexing/str-packed-rtree.md), a [filter-and-refine spatial join](algorithms/query-processing/filter-refine-spatial-join.md) and their tested Python examples.

A native [Clipper2 offsetting example](implementations/clipper2-csharp/README.md) complements the Shapely/GEOS route. A [coverage and advanced-routing lab](notebooks/coverage-simplification-routing-lab.ipynb) lets you inspect shared-edge simplification and compare directed shortest-path searches.

The weekly edition format is documented in the [newsletter issue template](docs/newsletter-issue-template.md).

**Current stage:** the compendium now has tested learning material across geometry, routing, spatial statistics, geostatistics, raster and terrain analysis, remote sensing, location science, decision support, GeoAI and geodesy. The repository inventory and CI status are tracked in the [roadmap](docs/repository-roadmap.md). All 22 source sections are indexed, but each source entry still needs appropriate verification, and many methods remain to be researched and implemented.
