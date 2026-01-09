import sys
from collections import defaultdict, deque

def count_sccs(n, edges):
    # Build adjacency list
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # Kosaraju's algorithm
    # Step 1: DFS on original graph to get finish times
    visited = [False] * (n + 1)
    finish_order = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        finish_order.append(node)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: DFS on reverse graph in reverse finish order
    visited = [False] * (n + 1)
    scc_count = 0
    
    def dfs2(node):
        visited[node] = True
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
    
    for node in reversed(finish_order):
        if not visited[node]:
            dfs2(node)
            scc_count += 1
    
    return scc_count

# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Count and print SCCs
print(count_sccs(n, edges))