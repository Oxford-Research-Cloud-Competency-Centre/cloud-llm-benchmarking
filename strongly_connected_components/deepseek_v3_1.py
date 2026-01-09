import sys
sys.setrecursionlimit(30000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    visited = [False] * (n+1)
    stack = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs1(i)
            
    visited = [False] * (n+1)
    
    def dfs2(node):
        visited[node] = True
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
    
    count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs2(node)
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()