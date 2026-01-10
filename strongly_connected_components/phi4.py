def count_sccs(n, m, edges):
    from collections import defaultdict

    def dfs(v, graph, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        stack.append(v)

    def reverse_graph(graph, n):
        reversed_graph = defaultdict(list)
        for u in range(1, n + 1):
            for v in graph[u]:
                reversed_graph[v].append(u)
        return reversed_graph

    def fill_order(graph, n):
        visited = [False] * (n + 1)
        stack = []
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i, graph, visited, stack)
        return stack

    def get_sccs(rev_graph, stack, n):
        visited = [False] * (n + 1)
        scc_count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                scc_stack = []
                dfs(v, rev_graph, visited, scc_stack)
                scc_count += 1
        return scc_count

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    stack = fill_order(graph, n)
    reversed_graph = reverse_graph(graph, n)
    return get_sccs(reversed_graph, stack, n)


# Example usage
n, m = 4, 4
edges = [(1, 2), (2, 3), (3, 1), (4, 1)]
print(count_sccs(n, m, edges))