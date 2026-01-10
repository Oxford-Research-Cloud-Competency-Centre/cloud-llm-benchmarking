import collections

def count_scc(n, edges):
    def dfs(graph, visited, order, node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, visited, order, neighbor)
        order.append(node)

    def dfs_reverse(graph, visited, component, node):
        visited.add(node)
        component.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_reverse(graph, visited, component, neighbor)

    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    order = []
    for i in range(1, n + 1):
        if i not in visited:
            dfs(graph, visited, order, i)

    rev_graph = collections.defaultdict(list)
    for u, v in edges:
        rev_graph[v].append(u)

    sccs = 0
    visited.clear()
    while order:
        node = order.pop()
        if node not in visited:
            component = set()
            dfs_reverse(rev_graph, visited, component, node)
            sccs += 1

    return sccs

# Input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(count_scc(n, edges))