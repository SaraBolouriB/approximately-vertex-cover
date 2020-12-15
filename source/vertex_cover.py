def calculate_degree(graph):
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

def isolated_vertex(graph):
    isolated_v = []
    vertices = len(graph[0])
    all_degrees = calculate_degree(graph)

    no_verex = 0
    iso_count = 0
    for vertex in range(vertices):
        if all_degrees[vertex] == -1:
            no_verex += 1
        elif all_degrees[vertex] == 0:
            iso_count += 1
            isolated_v.append(vertex+1)
    vertices -= no_verex
    is_iso = True if vertices == iso_count else False    
    return is_iso, isolated_v

def generate_H(G, S):
    '''
        1. Original graph is G = (V, E)
        2. Vertex-Cover set is S
        3. Generate graph H which is H = G - S
    '''
    lenS = len(S)
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
    '''
    lenG = len(G[0])
    L = list()
    isolated = iso_set
    for vertex in range(lenG):
        if vertex in S or vertex in isolated:
            L.append(vertex)
    return L
    
def find_leafage(graph):
    all_degrees = calculate_degree(graph=graph)
    leafages = list()
    index = 0
    for deg in all_degrees:
        if deg == 1:
            leafages.append(index)
        index += 1
    return leafages