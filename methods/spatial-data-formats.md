# Choosing spatial data formats and delivery patterns

A geospatial format is not a complete data architecture. Choose storage and delivery based on the data model, query pattern, update pattern, scale, client support and metadata needs. A format optimised for reading small windows from object storage may be a poor fit for frequent transactional edits.

## Match the format to the workload

| Data/workload | Useful format or standard | Why it fits | Important limitation |
|---|---|---|---|
| Large 2D raster imagery and regular grids | Cloud Optimized GeoTIFF (COG) | Tiled TIFF, overviews, georeferencing and HTTP range requests support partial reads at appropriate resolutions | Primarily a 2D raster asset; multi-dimensional time/band cubes may need another layout |
| Multidimensional arrays and data cubes | Zarr | Chunked, compressed arrays with metadata; supports cloud/object-store access patterns | Chunk shape and chunk-key layout must match query patterns |
| Large vector analytics and columnar processing | GeoParquet | Parquet columnar storage plus geospatial metadata and geometry encodings | Not a web-map tile format; spatial filtering depends on metadata, row-group layout and implementation |
| Streaming spatial subsets from a single vector file | FlatGeobuf | Binary feature records and optional spatial index support selective reads | Row-oriented; compression or repacking can affect random access; not a transactional database |
| Discovery across many spatial-temporal assets | STAC | Common Item, Collection and Catalog metadata and query interfaces describe assets by space, time and properties | STAC describes and discovers assets; it does not prescribe the internal raster/vector encoding |
| Pre-rendered web map delivery | Vector tiles / PMTiles | Compact tiled representation supports map display and efficient distribution | Tiles are a delivery product, not the authoritative editable feature store |
| Frequent updates, transactions and complex access control | Spatial database | Transactions, indexes, constraints and concurrent access support operational editing | Requires database operations, service design and performance management |

These categories overlap. A STAC Item may point to a COG, Zarr store, GeoParquet file, point cloud or derived tile product.

## Separate four architectural concerns

1. **Authoritative storage:** the dataset that defines the current accepted information and its provenance.
2. **Analytical layout:** the encoding optimised for the processing pattern, such as raster windows, array chunks or column scans.
3. **Discovery metadata:** identifiers, spatial/temporal extent, assets, licence, lineage and quality information.
4. **Delivery products:** tiles, previews, simplified geometries, cached subsets or application-specific exports.

Do not assume one physical file must satisfy every concern. Preserve a traceable relationship between derived products and their authoritative inputs.

## Chunking, tiling and query patterns

For raster and array data, choose tile/chunk dimensions based on typical window size, band count, time depth, compression, parallelism and expected request concurrency. Very small chunks increase metadata and request overhead; very large chunks force clients to read more data than they need.

For vector data, consider whether consumers read a few features, scan selected columns, filter by bounding box, or render a map. Spatially ordered row groups, bounding-box metadata and a spatial index can reduce unnecessary reads, but must be validated against the actual toolchain.

## Metadata is part of the data product

Record at least:
- stable dataset and item identifiers;
- geometry or spatial extent and CRS;
- temporal extent and acquisition/processing time where relevant;
- variable/band names, units, nodata and quality flags;
- source, lineage, processing steps and software versions;
- licence, access constraints and responsible organisation;
- resolution, scale or ground sample distance;
- known limitations, positional accuracy and completeness.

STAC provides a standardised way to describe discoverable assets. It does not remove the need to document the actual data schema or quality.

## A practical decision sequence

1. Identify the primary data model: raster, multidimensional array, vector, point cloud, network or rendered tile.
2. Identify the dominant operation: full scan, window read, spatial subset, column projection, time slice, rendering or transactional edit.
3. Identify the access environment: local disk, object storage, HTTP range, database or tile service.
4. Select a candidate format and confirm that the required clients support the features you need.
5. Choose tile/chunk/row-group layout using representative queries.
6. Validate coordinate reference metadata, nodata, geometry validity, temporal metadata and lineage.
7. Benchmark realistic reads and writes, including cold-cache and concurrent access.
8. Preserve an authoritative source and document how delivery products are regenerated.

## References and specifications

- OGC Cloud Optimized GeoTIFF Standard 1.0 (2023). https://docs.ogc.org/is/21-026/21-026.html
- OGC SpatioTemporal Asset Catalog (STAC) Community Standard 1.1.0. https://www.ogc.org/standards/stac/
- Cloud-Native Geospatial, *Cloud-Optimized Geospatial Formats Guide*. https://guide.cloudnativegeo.org/
- GDAL Raster Data Model. https://gdal.org/en/stable/user/raster_data_model.html

This is a format-selection guide, not a benchmark ranking. Verify format versions, extension support and client compatibility for each production workflow.
