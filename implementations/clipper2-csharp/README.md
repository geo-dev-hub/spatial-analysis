# Clipper2 native offsetting example (C#)

This small .NET 8 console project exercises Clipper2's native integer-path
offsetting API. It complements—but is deliberately separate from—the Python
Shapely/GEOS example.

## Run

```bash
dotnet run --project implementations/clipper2-csharp/Clipper2Example.csproj
```

The program checks a positive round offset, a negative miter offset and a
contraction that collapses the input rectangle. It exits with an exception if
an expected result is not observed, so it can run as a lightweight CI check.

## Coordinate scale is your responsibility

Clipper2's `Paths64` uses integer coordinates. If one coordinate unit is
intended to represent one millimetre, encode metres using a scale of 1,000.
Scale the offset distance consistently, check integer range and document the
chosen scale. The sample uses an arbitrary integer grid to make this explicit.

This example is for closed polygon paths (`EndType.Polygon`). Open-path end
caps are a separate API contract. Hole orientation, multiple output paths,
self-intersections and complex polygon-tree interpretation need additional
fixtures before using the wrapper on production data.

## Source and version

- NuGet package: [Clipper2](https://www.nuget.org/packages/Clipper2/), pinned here to 1.5.4.
- [Clipper2 official documentation](https://www.angusj.com/clipper2/Docs/Overview.htm).
- [ClipperOffset API](https://www.angusj.com/clipper2/Docs/Units/Clipper/Classes/ClipperOffset/ClipperOffset.htm).

The package version is explicit so a future upgrade can be reviewed and tested.
