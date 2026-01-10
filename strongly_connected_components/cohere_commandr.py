from collections import defaultdict, deque

def count_sccs(n, edges):
    # Initialize adjacency list and visited set
    adj_list = defaultdict(list)
    visited = set()

    # Build adjacency list
    for u, v in edges:
        adj_list[u].append(v)

    # Define a function to perform DFS
    def dfs(node):
        stack = [node]
        while stack:
            curr_node = stack.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                stack.extend(adj_list[curr_node])

    # Start DFS from each unvisited node
    scc_count = 0
    for i in range(1, n + 1):
        if i not in visited:
            dfs(i)
            scc_count += 1

    return scc_count

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Count SCCs
print(count_sccs(n, edges))