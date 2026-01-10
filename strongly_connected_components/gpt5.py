import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        print(0)
        return
    it = iter(data)
    try:
        n = next(it)
        m = next(it)
    except StopIteration:
        print(0)
        return

    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]

    for _ in range(m):
        try:
            u = next(it) - 1
            v = next(it) - 1
        except StopIteration:
            break
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(v)
            radj[v].append(u)

    visited = [False] * n
    order = []

    for start in range(n):
        if visited[start]:
            continue
        stack = [(start, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for nei in adj[node]:
                    if not visited[nei]:
                        stack.append((nei, 0))
            else:
                order.append(node)

    visited2 = [False] * n
    scc_count = 0

    for start in reversed(order):
        if visited2[start]:
            continue
        scc_count += 1
        stack = [start]
        visited2[start] = True
        while stack:
            node = stack.pop()
            for nei in radj[node]:
                if not visited2[nei]:
                    visited2[nei] = True
                    stack.append(nei)

    print(scc_count)

if __name__ == "__main__":
    main()