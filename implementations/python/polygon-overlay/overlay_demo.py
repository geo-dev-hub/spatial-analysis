from shapely import Polygon
from polygon_overlay import describe_result, overlay

a = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
b = Polygon([(2, -1), (5, -1), (5, 2), (2, 2)])
for operation in ("intersection", "union", "difference", "symmetric_difference"):
    result = overlay(a, b, operation)
    report = describe_result(result)
    print(f"{operation}: {report['geometry_type']}, area={report['area']:.1f}, valid={report['is_valid']}")
