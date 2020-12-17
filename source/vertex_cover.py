from dijkstra import *
from component import *
import random

def compute_vertex_cover(init, graph):
    vertices = len(graph[0])                    # Number of graph vertices 
    init -= 1                                   # Index of initial point
    ## Step 1 ------------------------------------------------------------------------------------------------------
    S, Ss, L, T, dist, isolated_v = [], [], [], [], [], []
    is_disjoint, is_isolated = False, False
    S.append(init)                              # Add First vertex to VC set
    #---------------------------------------------------------------------------------------------------------------
                  
    ## Step 2 ------------------------------------------------------------------------------------------------------
    H = generate_H(G=graph, S=S)                 # H = graph - S 
    is_isolated, isolated_v = is_isolated_graph(H) # whether all vertices of H are isolated or not.

    while not is_isolated and not is_disjoint:

        ## Find Leafage
        leafages = find_leafage(graph=H)
        if len(leafages) != 0:
            for l in leafages:
                parent_node = H[l].index(1)
                S.append(parent_node)
        ## No leafages have found
        else:
            L = generate_L(G=graph, S=S, iso_set=isolated_v)
            Hh = generate_H(G=graph, S=Ss) 

            if is_isolated_vertex(init, Hh):
                S.append(random.choice(L))
            else:
                Ss.append(init)
                dist = dijkstra(source=init, graph=graph, graphL=L)
                d = max(dist)
                if d > 1:
                    d -= 1
                    T = [ i for i in range(vertices) if dist[i] == d ]
                    all_cc_counts = list()
                    for vertex in T:
                        new_graph = generate_H(H=H, S=[vertex])
                        cc_count = connectedComponents(graph=new_graph)
                        all_cc_counts.append(cc_count)
                    if all_the_same(all_cc_counts):
                        degree_T = calculate_degree(graph=T)
                        if all_the_same(degree_T):
                            init = min(T) # vertex with minimum label
                        else:
                            init = degree_t.index(max(degree_T)) # vertex with maximum degree
                    else:
                        init = all_cc_counts.index(min(all_cc_counts)) # vertex with minimum connectec component


                    S.append(init)
                elif d == 1:
                    H = generate_H(G=graph, S=S)
                    cc_count = connectedComponents(graph=H)
                    if len(cc_count) != 1:
                        is_disjoint = True
                    else:
                        degree_H = calculate_degrees(graph=H)
                        if all_the_same(degree_H):
                            init = min(L)
                        else:
                            init = degree_H.index(max(degree_H))
                            S.append(init)
            
        H = generate_H(G=graph, S=S)
        is_isolated, isolated_v = is_isolated_graph(H)

    return S

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
        if vertex not in S or vertex not in iso_set:
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