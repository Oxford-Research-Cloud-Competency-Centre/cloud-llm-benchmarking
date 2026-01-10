import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n+1)]
    reversed_adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        adj[u].append(v)
        reversed_adj[v].append(u)
    
    visited = [False] * (n+1)
    finishing_order = []
    
    for node in range(1, n+1):
        if not visited[node]:
            stack = []
            stack.append((node, 0))
            while stack:
                current, idx = stack.pop()
                if idx == 0:
                    visited[current] = True
                neighbors = adj[current]
                if idx < len(neighbors):
                    stack.append((current, idx + 1))
                    next_node = neighbors[idx]
                    if not visited[next_node]:
                        stack.append((next_node, 0))
                else:
                    finishing_order.append(current)
    
    visited = [False] * (n+1)
    scc_count = 0
    
    for node in reversed(finishing_order):
        if not visited[node]:
            scc_count += 1
            stack = [node]
            visited[node] = True
            while stack:
                current = stack.pop()
                for neighbor in reversed_adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    print(scc_count)

if __name__ == "__main__":
    main()