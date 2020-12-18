def calculate_degrees_T(indexList, graph):
    all_degree = calculate_degrees(graph=graph)
    degree_T = [all_degree[i] for i in range(len(graph[0])) if i in indexList]
    return degree_T

def calculate_degrees(graph):
    lenG = len(graph[0])
    degree = [0 for i in range(lenG)]

    for v in range(lenG):
        deg = 0
        if graph[v][0] == -1:
            deg = -1
        else:
            for u in range(lenG):
                if graph[v][u] > 0 :
                    deg += 1
        degree[v] = deg
    return degree

def is_isolated_vertex(vertex, graph):
    no_edges = graph[vertex].count(0)
    vertices = len(graph[0])
    return True if no_edges == vertices else False

def is_isolated_graph(graph):
    isolated_v = []             # Isolated vertices set
    vertices = len(graph[0])    # Number of all vertices of orginal graph
    all_degrees = calculate_degrees(graph=graph)

    no_verex = 0                # Number of vertices which are removed from graph
    iso_count = 0               # Number of isolated vertices
    for vertex in range(vertices):
        if all_degrees[vertex] == -1:
            no_verex += 1
        elif all_degrees[vertex] == 0:
            iso_count += 1
            isolated_v.append(vertex)
    vertices -= no_verex
    is_iso = True if vertices == iso_count else False    
    return is_iso, isolated_v

def generate_H(G, S):
    '''
        1. Original graph is G = (V, E)
        2. Vertex-Cover set is S
        3. Generate graph H which is H = G - S
    '''
    G = list(map(list, G))
    lenG = len(G[0])
    for s in S:
        for vertex in range(lenG):
            if G[s][vertex] == 1:
                G[s][vertex] = -1
                G[vertex][s] = 0
            else:
                G[s][vertex] = -1
    return G

def generate_L(G, S, iso_set):
    '''
        1. Original graph is G = (V, E)
        2. Vertex-Cover set is S
        3. H = G - S
        4. Generate graph L which is L = V - S - {isolated verices of H}
        5. Index of each vertices are saved in L
    '''
    lenG = len(G[0])
    L = list()
    for vertex in range(lenG):
        if vertex not in S and vertex not in iso_set:
            L.append(vertex)
    return L
    
def find_leafage(graph):
    all_degrees = calculate_degrees(graph=graph)
    leafages = list()
    index = 0
    for deg in all_degrees:
        if deg == 1:
            leafages.append(index)
        index += 1
    return leafages

def all_the_same(elements):
   if len(elements) < 1:
       return True
   return len(elements) == elements.count(elements[0])

def sub_graph(vertices, graph):
    graph = list(map(list, graph))
    lenG = len(graph[0])
    for v in range(lenG):
        if v not in vertices:
            for u in range(lenG):
                graph[v][u] = -1
                graph[u][v] = 0
    return graph

def remove_parent(leafages, H):
    parents = []
    leafs = []
    for l in leafages:
        leafs.append(l)
        parent_node = H[l].index(1)
        if parent_node not in parents and parent_node not in leafs:
            parents.append(parent_node)
            
    return parents