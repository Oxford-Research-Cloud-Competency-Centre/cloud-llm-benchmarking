import sys
from collections import defaultdict

def kosaraju_scc(n, edges):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    # Build the graph and reverse graph
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # First pass: DFS to get finish times
    visited = [False] * (n + 1)
    finish_order = []
    
    def dfs1(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs1(neighbor)
        finish_order.append(v)
    
    for v in range(1, n + 1):
        if not visited[v]:
            dfs1(v)
    
    # Second pass: DFS on reverse graph in reverse finish order
    visited = [False] * (n + 1)
    scc_count = 0
    
    def dfs2(v):
        visited[v] = True
        for neighbor in reverse_graph[v]:
            if not visited[neighbor]:
                dfs2(neighbor)
    
    # Process vertices in reverse order of their finish times
    for v in reversed(finish_order):
        if not visited[v]:
            dfs2(v)
            scc_count += 1
    
    return scc_count

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    print(kosaraju_scc(n, edges))

if __name__ == "__main__":
    main()