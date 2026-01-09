def kosaraju_scc(graph, n):
    def dfs1(v, visited, stack):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs1(u, visited, stack)
        stack.append(v)
    
    def dfs2(v, visited, rev_graph):
        visited[v] = True
        for u in rev_graph[v]:
            if not visited[u]:
                dfs2(u, visited, rev_graph)
    
    rev_graph = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        for u in graph[v]:
            rev_graph[u].append(v)
    
    visited = [False] * (n + 1)
    stack = []
    for v in range(1, n + 1):
        if not visited[v]:
            dfs1(v, visited, stack)
    
    visited = [False] * (n + 1)
    scc_count = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            dfs2(v, visited, rev_graph)
            scc_count += 1
            
    return scc_count

def main():
    n, m = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    result = kosaraju_scc(graph, n)
    print(result)

if __name__ == "__main__":
    main()