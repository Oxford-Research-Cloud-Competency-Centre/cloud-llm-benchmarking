import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    reverse_adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        reverse_adj[v].append(u)

    visited = [False] * (N + 1)
    stack = []

    for u in range(1, N + 1):
        if not visited[u]:
            stack_iter = [(u, False)]
            while stack_iter:
                node, flag = stack_iter.pop()
                if not flag:
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack_iter.append((node, True))
                    for v in adj[node]:
                        if not visited[v]:
                            stack_iter.append((v, False))
                else:
                    stack.append(node)

    visited2 = [False] * (N + 1)
    count = 0

    while stack:
        u = stack.pop()
        if not visited2[u]:
            count += 1
            stack2 = [u]
            visited2[u] = True
            while stack2:
                node = stack2.pop()
                for v in reverse_adj[node]:
                    if not visited2[v]:
                        visited2[v] = True
                        stack2.append(v)

    print(count)

if __name__ == "__main__":
    main()