using Clipper2Lib;
using Tessellatum.SpatialAnalysis;

static void Require(bool condition, string message)
{
    if (!condition) throw new InvalidOperationException(message);
}

var rectangle = new Path64
{
    new Point64(0, 0),
    new Point64(1000, 0),
    new Point64(1000, 600),
    new Point64(0, 600)
};
var input = new Paths64 { rectangle };

var expanded = Offsetter.OffsetClosedPaths(input, 100, JoinType.Round);
Require(expanded.Count == 1, "Expected one expanded rectangle path.");
Require(expanded[0].Count > rectangle.Count, "Round joins should add arc vertices.");

var contracted = Offsetter.OffsetClosedPaths(input, -100, JoinType.Miter);
Require(contracted.Count == 1, "Expected one contracted rectangle path.");

var collapsed = Offsetter.OffsetClosedPaths(input, -400, JoinType.Miter);
Require(collapsed.Count == 0, "A contraction larger than the half-width should collapse this rectangle.");

Console.WriteLine("Clipper2 offset checks passed.");
Console.WriteLine($"Input vertices: {rectangle.Count}; round-offset vertices: {expanded[0].Count}");
