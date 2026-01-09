import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    adj = [[] for _ in range(n + 1)]
    reverse_adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].append(v)
        reverse_adj[v].append(u)
    
    visited = [False] * (n + 1)
    order = []
    
    def dfs(u):
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            for v in adj[node]:
                if not visited[v]:
                    stack.append((v, False))
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    visited = [False] * (n + 1)
    count = 0
    
    def reverse_dfs(u):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            for v in reverse_adj[node]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
    
    for node in reversed(order):
        if not visited[node]:
            reverse_dfs(node)
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()