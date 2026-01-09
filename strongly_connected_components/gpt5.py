import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        print(0)
        return

    if len(data) == 1:
        N = data[0]
        M = 0
        edges_data = []
    else:
        N, M = data[0], data[1]
        edges_data = data[2:]

    adj = [[] for _ in range(N + 1)]
    radj = [[] for _ in range(N + 1)]

    idx = 0
    for _ in range(M):
        if idx + 1 >= len(edges_data):
            break
        u = edges_data[idx]
        v = edges_data[idx + 1]
        idx += 2
        if 1 <= u <= N and 1 <= v <= N:
            adj[u].append(v)
            radj[v].append(u)

    visited = [False] * (N + 1)
    top_order = []

    for start in range(1, N + 1):
        if not visited[start]:
            visited[start