from collections import defaultdict

def SCC(graph):
    stack = []
    SCCs = 0
    visited = [False] * (len(graph) + 1)
    stackMember = [False] * (len(graph) + 1)
    discovery = [float("Inf")] * (len(graph) + 1)
    low = [float("Inf")] * (len(graph) + 1)
    time = 0

    def SCCUtil(u):
        nonlocal time
        discovery[u] = time
        low[u] = time
        time += 1
        stack.append(u)
        stackMember[u] = True

        for v in graph[u]:

            if discovery[v] == float("Inf"):
                SCCUtil(v)
                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:
                low[u] = min(low[u], discovery[v])

        w = -1
        if low[u] == discovery[u]:
            nonlocal SCCs
            while w != u:
                w = stack.pop()
                stackMember[w] = False
            SCCs += 1

    for i in range(1, len(graph) + 1):
        if discovery[i] == float("Inf"):
            SCCUtil(i)

    return SCCs


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
print(SCC(graph))