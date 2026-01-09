from collections import defaultdict

def count_scc(n, edges):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            fill_stack(i, graph, visited, stack)

    visited = [False] * (n + 1)
    count = 0
    while stack:
        i = stack.pop()
        if not visited[i]:
            dfs(i, reverse_graph, visited)
            count += 1

    return count

def fill_stack(v, graph, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            fill_stack(neighbor, graph, visited, stack)
    stack.append(v)

def dfs(v, graph, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

def main():
    try:
        n, m = map(int, input().split())
        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u, v))
        print(count_scc(n, edges))
    except EOFError:
        pass

if __name__ == "__main__":
    main()