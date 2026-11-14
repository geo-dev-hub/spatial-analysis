using Clipper2Lib;

namespace Tessellatum.SpatialAnalysis;

public static class Offsetter
{
    /// <summary>
    /// Offset closed polygon paths using Clipper2's integer-coordinate engine.
    /// The caller is responsible for selecting and documenting a scale factor.
    /// </summary>
    public static Paths64 OffsetClosedPaths(
        Paths64 paths,
        double delta,
        JoinType joinType = JoinType.Round,
        double miterLimit = 2.0,
        double arcTolerance = 0.25)
    {
        ArgumentNullException.ThrowIfNull(paths);
        if (!double.IsFinite(delta))
            throw new ArgumentOutOfRangeException(nameof(delta), "Offset distance must be finite.");
        if (!double.IsFinite(miterLimit) || miterLimit <= 0)
            throw new ArgumentOutOfRangeException(nameof(miterLimit), "Miter limit must be finite and positive.");
        if (!double.IsFinite(arcTolerance) || arcTolerance < 0)
            throw new ArgumentOutOfRangeException(nameof(arcTolerance), "Arc tolerance must be finite and non-negative.");

        var offsetter = new ClipperOffset(miterLimit, arcTolerance);
        offsetter.AddPaths(paths, joinType, EndType.Polygon);
        var solution = new Paths64();
        offsetter.Execute(delta, solution);
        return solution;
    }
}
