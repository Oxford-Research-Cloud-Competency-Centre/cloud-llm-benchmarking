import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        radj[v].append(u)

    visited = [False] * (n + 1)
    order = []

    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [start]
        while stack:
            v = stack.pop()
            if v > 0:
                if visited[v]:
                    continue
                visited[v] = True
                stack.append(-v)  # marker for post-visit
                for nei in adj[v]:
                    if not visited[nei]:
                        stack.append(nei)
            else:
                order.append(-v)

    visited = [False] * (n + 1)
    scc_count = 0

    for v in reversed(order):
        if visited[v]:
            continue
        scc_count += 1
        stack = [v]
        visited[v] = True
        while stack:
            u = stack.pop()
            for nei in radj[u]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

    print(scc_count)

if __name__ == "__main__":
    main()