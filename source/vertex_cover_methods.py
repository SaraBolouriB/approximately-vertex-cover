def calculate_degrees_list(indexList, graph, lenG):
    all_degree = calculate_degrees(graph=graph, lenG=lenG)
    degree_T = [all_degree[i] for i in range(lenG) if i in indexList]
    return degree_T
##
def calculate_degrees(graph, lenG):
    degree = [0 for i in range(lenG)]

    for v in range(lenG):
        deg = 0
        if not graph[v]:
            deg = 0
        elif graph[v][0] == -1:
            deg = -1
        else:
            deg = len(graph[v])
        degree[v] = deg
    return degree
##
def is_isolated_vertex(vertex, graph):
    no_edges = len(graph[vertex])
    return True if no_edges == 0 else False
##
def is_isolated_graph(graph, lenG):
    isolated_v = []             # Isolated vertices set
    all_degrees = calculate_degrees(graph=graph, lenG=lenG)

    no_verex = 0                # Number of vertices which are removed from graph
    iso_count = 0               # Number of isolated vertices
    for vertex in range(lenG):
        if all_degrees[vertex] == -1:
            no_verex += 1
        elif all_degrees[vertex] == 0:
            iso_count += 1
            isolated_v.append(vertex)
    lenG -= no_verex
    is_iso = True if lenG == iso_count else False    
    return is_iso, isolated_v
##
def generate_H(graph, S, lenG):
    '''
        1. Original graph is G = (V, E)
        2. Vertex-Cover set is S
        3. Generate graph H which is H = G - S
    '''
    graph = list(map(list, graph))
    for s in S:
        nodes = graph[s]
        for node in nodes:
            graph[node].remove(s) 
        graph[s] = [-1]
    return graph
##
def generate_L(G, S, iso_set, lenG):
    '''
        1. Original graph is G = (V, E)
        2. Vertex-Cover set is S
        3. H = G - S
        4. Generate graph L which is L = V - S - {isolated verices of H}
        5. Index of each vertices are saved in L
    '''
    L = list()
    for vertex in range(lenG):
        if vertex not in S and vertex not in iso_set and G[vertex][0] != -1:
            L.append(vertex)
    return L
##
def find_leafage(graph, lenG):
    all_degrees = calculate_degrees(graph=graph, lenG=lenG)
    leafages = list()
    index = 0
    for deg in all_degrees:
        if deg == 1:
            leafages.append(index)
        index += 1
    return leafages
##
def remove_parent(leafages, H):
    parents = []
    leafs = []
    for l in leafages:
        leafs.append(l)
        parent_node = H[l][0]
        if parent_node not in parents and parent_node not in leafs:
            parents.append(parent_node)
            
    return parents

def all_the_same(elements):
   if len(elements) < 1:
       return True
   return len(elements) == elements.count(elements[0])
##
def sub_graph(vertices, graph, lenG):
    sub_graph = []

    for v in range(lenG):
        if v not in vertices:
            sub_graph.append([-1])
        else:
            edges = []
            nodes = graph[v]
            for n in nodes:
                if n in vertices:
                    edges.append(n)
            sub_graph.append(edges)
    return sub_graph