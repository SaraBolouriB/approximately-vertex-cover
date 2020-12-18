from dijkstra import *
from component import *
import random
from methods import *

def compute_vertex_cover(init, graph):
    original_graph = tuple(map(tuple, graph))

    vertices = len(original_graph[0])                        # Number of graph vertices 
    init -= 1                                                # Index of initial point
    ## Step 1 ------------------------------------------------------------------------------------------------------
    S, Ss, L, T, dist, isolated_v = [], [], [], [], [], []
    is_disjoint, is_isolated = False, False
    S.append(init)                                          # Add First vertex to VC set
    #---------------------------------------------------------------------------------------------------------------
                  
    ## Step 2 ------------------------------------------------------------------------------------------------------
    H = generate_H(G=original_graph, S=S)          
    is_isolated, isolated_v = is_isolated_graph(H)  # whether all vertices of H are isolated or not.

    while not is_isolated and not is_disjoint:

        # Find Leafage
        leafages = find_leafage(graph=H)
        if len(leafages) != 0:
            parents = []
            leafs = []
            for l in leafages:
                leafs.append(l)
                parent_node = H[l].index(1)
                if parent_node not in parents and parent_node not in leafs:
                    parents.append(parent_node)
                    S.append(parent_node)
                    Ss.append(parent_node)
    #---------------------------------------------------------------------------------------------------------------
    ## Step 3 ------------------------------------------------------------------------------------------------------
        # No leafages have found
        else:
            L = generate_L(G=original_graph, S=S, iso_set=isolated_v)
            Hh = generate_H(G=original_graph, S=Ss)          # Calculated H without init
            if is_isolated_vertex(init, Hh):
                init = random.choice(L)
                S.append(init)
            else:
                Ss.append(init)
                dist = dijkstra(source=init, graph=original_graph, graphL=L)
                d = max(dist)
                if d > 1:
                    d -= 1
                    T = [ i for i in range(vertices) if dist[i] == d ]
                    all_cc_counts = list()
                    for vertex in T:
                        new_graph = generate_H(G=H, S=[vertex])
                        cc_count, cc = connectedComponents(graph=new_graph)
                        all_cc_counts.append(cc_count)
                    if all_the_same(all_cc_counts):
                        degree_T = calculate_degrees_T(indexList=T, graph=H)
                        if all_the_same(degree_T):
                            init = min(T) # vertex with minimum label
                        else:
                            index = degree_T.index(max(degree_T)) # vertex with maximum degree
                            init = T[index]
                    else:
                        index = all_cc_counts.index(min(all_cc_counts)) # vertex with minimum connectec component
                        init = T[index]

                    S.append(init)
                elif d == 1:
                    H = generate_H(G=graph, S=S)
                    cc_count, cc = connectedComponents(graph=H)
                    if cc_count != 1:
                        is_disjoint = True
                    else:
                        degree_H = calculate_degrees(graph=H)
                        if all_the_same(degree_H):
                            init = min(L)
                        else:
                            init = degree_H.index(max(degree_H))
                            S.append(init)
        ## Step 2 ------------------------------------------------------------------------------------------------------
        H = generate_H(G=original_graph, S=S)
        is_isolated, isolated_v = is_isolated_graph(H)
        for iso in isolated_v:
            if iso not in Ss:
                Ss.append(iso)
        # --------------------------------------------------------------------------------------------------------------

    return S

