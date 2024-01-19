class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal_mst(self):
        self.graph.sort(key=lambda edge: edge[2])
        parent = list(range(self.V))

        def find(i):
            return i if parent[i] == i else find(parent[i])

        def union(i, j):
            parent[find(i)] = find(j)

        result = []

        for edge in self.graph:
            u, v, w = edge
            if find(u) != find(v):
                result.append(edge)
                union(u, v)

        return result

num_vertices = int(input("Enter the number of vertices: "))
g = Graph(num_vertices)

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, w = map(int, input("Enter edge (u v w) separated by space: ").split())
    g.add_edge(u, v, w)

mst = g.kruskal_mst()

print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} == {edge[2]}")

