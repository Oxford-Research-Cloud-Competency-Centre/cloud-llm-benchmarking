import sys
sys.setrecursionlimit(1000000)

def kosaraju(n, edges):
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    
    for u, v in edges:
        graph[u-1].append(v-1)
        reverse_graph[v-1].append(u-1)
    
    visited = [False] * n
    order = []
    
    def dfs1(v):
        visited[v] = True
        for to in graph[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * n
    components = 0
    
    def dfs2(v):
        visited[v] = True
        for to in reverse_graph[v]:
            if not visited[to]:
                dfs2(to)
    
    for v in reversed(order):
        if not visited[v]:
            dfs2(v)
            components += 1
    
    return components

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m = map(int, data[:2])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        edges.append((u, v))
        idx += 2
    result = kosaraju(n, edges)
    print(result)

if __name__ == "__main__":
    main()