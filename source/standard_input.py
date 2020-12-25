from igraph import *

def generate_random_graph(node, edge):
    g = Graph.Erdos_Renyi(n=node, m=edge)
    graph = [[-1] for row in range(node)]
    edges = g.get_edgelist()

    for edge in edges:
        a = edge[0]
        b = edge[1]

        graph[a].append(b)
        if -1 in graph[a]:
            graph[a].remove(-1)

        graph[b].append(a)
        if -1 in graph[b]:
            graph[b].remove(-1)

    return graph
