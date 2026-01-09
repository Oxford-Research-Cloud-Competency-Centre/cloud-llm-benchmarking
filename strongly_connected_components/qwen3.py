import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # Step 1: First DFS on original graph to get finishing times
    visited = [False] * (n + 1)
    order = []
    
    def dfs1(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs1(u)
        order.append(v)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Step 2: DFS on reverse graph in reverse finishing order
    visited = [False] * (n + 1)
    scc_count = 0
    
    def dfs2(v, component):
        visited[v] = True
        component.append(v)
        for u in reverse_graph[v]:
            if not visited[u]:
                dfs2(u, component)
    
    # Process vertices in reverse order of finishing times
    for v in reversed(order):
        if not visited[v]:
            component = []
            dfs2(v, component)
            scc_count += 1
    
    print(scc_count)

solve()