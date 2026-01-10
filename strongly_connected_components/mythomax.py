def scc(graph):
    """
    Function to find the strongly connected components of a directed graph.
    """
    # Initialize the graph as a dictionary where each node is a list of its neighboring nodes
    G = {}
    for i in range(len(graph)):
        G[i] = []

    # Add all nodes to the first SCC
    SCC = []
    SCC.append(0)

    # Iterate through the graph
    for i in range(1, len(graph)):
        # If the node is already in a SCC, find its SCC number
        if i in G:
            SCC = []
            for j in G[i]:
                if j not in SCC:
                    SCC.append(j)
                    SCC.append(i)
                    G[j].remove(i)
                    if len(G[j]) == 0:
                        SCC[len(SCC) // 2] = len(SCC) - 1
                        SCC.remove(len(SCC) // 2)
                        SCC.remove(len(SCC) // 2)
                        G[j].append(G[len(SCC) // 2])
                        G[len(SCC) // 2].remove(i)

    # Return the number of SCCs
    return len(set(SCC))

def main():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]

    print(scc(graph))

if __name__ == "__main__":
    main()