from voronoi_delaunay import build_tessellations

sites = [(0, 0), (4, 0), (4, 3), (0, 3), (2, 1)]
result = build_tessellations(sites)
print("Delaunay triangles (site indices):")
print(result.delaunay.simplices)
print("Voronoi vertices:")
print(result.voronoi.vertices)
