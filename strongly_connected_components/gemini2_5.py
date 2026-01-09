import sys

sys.setrecursionlimit(200005)

def main():
    """
    Main function to read graph input and count strongly connected components.
    """
    first_line = sys.stdin.readline()
    if not first_line.strip():
        print(0)
        return

    try:
        N, M = map(int, first_line.split())
    except (ValueError, IndexError):
        print(0)
        return
        
    if N == 0:
        print(0)
        return

    adj = [[] for _ in range(N + 1)]
    rev_adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        try:
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            rev_adj[v].append(u)
        except (ValueError, IndexError):
            continue

    # --- Kosaraju's Algorithm ---

    # Step 1: Perform DFS on the original graph to get the finishing order of vertices.
    visited = [False] * (N + 1)
    order_stack = []

    def dfs_order(node):
        """Fills the order_stack with vertices in post-order."""
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs_order(neighbor)
        order_stack.append(node)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs_order(i)

    # Step 2: Perform DFS on the transpose graph in the order determined by the stack.
    visited = [False] * (N + 1)
    scc_count = 0

    def dfs_scc(node):
        """Marks all vertices in the current SCC as visited."""
        visited[node] = True
        for neighbor in rev_adj[node]:
            if not visited[neighbor]:
                dfs_scc(neighbor)

    while order_stack:
        node = order_stack.pop()
        if not visited[node]:
            scc_count += 1
            dfs_scc(node)

    print(scc_count)

if __name__ == "__main__":
    main()