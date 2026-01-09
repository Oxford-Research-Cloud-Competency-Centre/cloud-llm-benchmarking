from collections import defaultdict, deque

def tarjans_scc(n):
    index = 0
    indices = [-1] * n
    low_links = [-1] * n
    st = []
    scc_count = 0
    stack_member = [False] * n
    sccs_list = []

    def strongconnect(v):
        nonlocal index, scc_count
        indices[v] = low_links[v] = index
        index += 1
        st.append(v)
        stack_member[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                low_links[v] = min(low_links[v], low_links[w])
            elif stack_member[w]:
                low_links[v] = min(low_links[v], indices[w])

        if low_links[v] == indices[v]:
            scc = []
            while True:
                w = st.pop()
                stack_member[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs_list.append(scc)
            scc_count += 1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)

    return scc_count

# Input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(tarjans_scc(n))