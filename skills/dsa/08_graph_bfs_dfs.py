"""
08 - Graph Traversals (BFS & DFS)
===================================
Adjacency-list graph with Breadth-First Search, Depth-First Search,
and a shortest-path finder using BFS.

Key Concepts:
    - Graph representation (adjacency list)
    - BFS — level-order exploration using a queue
    - DFS — deep exploration using recursion / stack
    - Shortest path in unweighted graphs
"""

from collections import deque


class Graph:
    """Undirected graph using an adjacency list."""

    def __init__(self):
        self._adj = {}

    def add_vertex(self, vertex):
        if vertex not in self._adj:
            self._adj[vertex] = []

    def add_edge(self, u, v):
        """Add an undirected edge between u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self._adj[u]:
            self._adj[u].append(v)
        if u not in self._adj[v]:
            self._adj[v].append(u)

    def vertices(self):
        return list(self._adj.keys())

    def neighbors(self, vertex):
        return self._adj.get(vertex, [])

    def bfs(self, start):
        """Breadth-First Search from a starting vertex. Returns visit order."""
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self._adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        """Depth-First Search (iterative) from a starting vertex."""
        visited = set()
        order = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                # Add neighbors in reverse for consistent ordering
                for neighbor in reversed(self._adj[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order

    def shortest_path(self, start, end):
        """Find the shortest path between two vertices using BFS."""
        if start == end:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            vertex, path = queue.popleft()
            for neighbor in self._adj[vertex]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    if neighbor == end:
                        return new_path
                    visited.add(neighbor)
                    queue.append((neighbor, new_path))

        return []  # No path found

    def __repr__(self):
        lines = [f"  {v} -> {neighbors}" for v, neighbors in self._adj.items()]
        return "Graph:\n" + "\n".join(lines)


if __name__ == "__main__":
    g = Graph()
    edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
        ("C", "F"), ("D", "G"), ("E", "G"), ("F", "G"),
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print(g)

    print(f"\nBFS from 'A': {g.bfs('A')}")
    print(f"DFS from 'A': {g.dfs('A')}")

    path = g.shortest_path("A", "G")
    print(f"\nShortest path A -> G: {' -> '.join(path)} (length: {len(path) - 1})")

    path2 = g.shortest_path("C", "D")
    print(f"Shortest path C -> D: {' -> '.join(path2)} (length: {len(path2) - 1})")
