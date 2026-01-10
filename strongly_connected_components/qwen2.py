from collections import defaultdict
from typing import List, Tuple

class Graph:
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def dfs_util(self, v: int, visited: List[bool]):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def fill_order(self, v: int, visited: List[bool], stack: List[int]):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def reverse_graph(self) -> 'Graph':
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def count_strongly_connected_components(self) -> int:
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        gr = self.reverse_graph()

        visited = [False] * self.V
        count = 0

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs_util(i, visited)
                count += 1

        return count

def count_scc(n: int, edges: List[Tuple[int, int]]) -> int:
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)
    return g.count_strongly_connected_components()

# Example usage:
if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(count_scc(n, edges))