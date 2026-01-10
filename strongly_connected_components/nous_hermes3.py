from collections import defaultdict

def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    return reversed_graph

def dfs_scc(graph, node, visited, scc):
    visited[node] = True
    scc.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_scc(graph, neighbor, visited, scc)

def count_scc(graph, n):
    visited = [False] * (n + 1)
    stack = []
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, node, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited = [False] * (n + 1)
    scc_count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_scc(reversed_graph, node, visited, scc)
            scc_count += 1
    return scc_count

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# Count strongly connected components
result = count_scc(graph, n)
print(result)