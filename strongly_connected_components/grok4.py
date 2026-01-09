import sys

sys.setrecursionlimit(100000)

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

graph = [[] for _ in range(N + 1)]
transpose = [[] for _ in range(N + 1)]

for _ in range(M):
    u = int(data[index])
    index += 1
    v = int(data[index])
    index += 1
    graph[u].append(v)
    transpose[v].append(u)

visited = [False] * (N + 1)
stack = []

def dfs1(node):
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs1(nei)
    stack.append(node)

for i in range(1, N + 1):
    if not visited[i]:
        dfs1(i)

visited = [False] * (N + 1)

def dfs2(node):
    visited[node] = True
    for nei in transpose[node]:
        if not visited[nei]:
            dfs2(nei)

count = 0
while stack:
    node = stack.pop()
    if not visited[node]:
        dfs2(node)
        count += 1

print(count)