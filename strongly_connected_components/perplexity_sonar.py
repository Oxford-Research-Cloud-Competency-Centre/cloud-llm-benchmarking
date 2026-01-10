import sys
sys.setrecursionlimit(2000000)

def kosaraju_scc_count(n, edges):
    g = [[] for _ in range(n)]
    gt = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        g[u].append(v)
        gt[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    scc_count = 0

    def dfs2(v):
        visited[v] = True
        for to in gt[v]:
            if not visited[to]:
                dfs2(to)

    for v in reversed(order):
        if not visited[v]:
            scc_count += 1
            dfs2(v)

    return scc_count

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    result = kosaraju_scc_count(n, edges)
    print(result)

if __name__ == "__main__":
    main()