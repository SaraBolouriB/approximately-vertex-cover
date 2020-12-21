from dijkstra import *
from component import *
import random
from vertex_cover_methods import *

def compute_vertex_cover(init, original_graph):

    vertices = len(original_graph[0])                                       # Number of graph vertices 

    ## Step 1 ------------------------------------------------------------------------------------------------------
    # Initializing -------------------------------------------------------------------------------------------------
    S, Ss, L, T, dist, isolated_v = [], [], [], [], [], []
    is_disjoint, is_isolated = False, False
    S.append(init)                                                          # Add the first vertex to S
    # End initializing ---------------------------------------------------------------------------------------------

    while True:
        H = generate_H(graph=original_graph, S=S)                           # Generate H = graph - S  
        is_isolated, isolated_v = is_isolated_graph(H)                      # Return check result and isolated vertices

        Ss.extend([iso for iso in isolated_v if iso not in Ss])             # Update Ss set

    ### End of the algorithm ### -----------------------------------------------------------------------------------
        if is_isolated:
            return S                                                        # Return vertex-cover set (S)
    ## Step 2 ------------------------------------------------------------------------------------------------------
        is_disjoint, components = connectedComponents(graph=H)              # Return check result and all components set

        if is_disjoint != 1:                                                # if it is true, algorithm will be run for each component 
            for component in components:
                sub_G = sub_graph(vertices=component, graph=original_graph)
                vc = compute_vertex_cover(init=random.choice(component), original_graph=sub_G)
                S.extend(vc)
                Ss.extend(vc)
    
        else:
            leafages = find_leafage(graph=H)
            if len(leafages) != 0:
                parents = remove_parent(leafages=leafages, H=H)
                S.extend(parents)
                Ss.extend(parents)
    # --------------------------------------------------------------------------------------------------------------
    ## Step 3 ------------------------------------------------------------------------------------------------------
            else:
                L = generate_L(G=original_graph, S=S, iso_set=isolated_v)
                Hh = generate_H(graph=original_graph, S=Ss)                     # calculated H without init

                if is_isolated_vertex(init, Hh):
                    degree_L = calculate_degrees_list(indexList=L, graph=H)
                    index = degree_L.index(max(degree_L))                       # vertex with maximum degree in L
                    init = L[index]
                    S.append(init)
                else:
                    Ss.append(init)
                    dist = dijkstra(source=init, graph=original_graph, graphL=L)
    # --------------------------------------------------------------------------------------------------------------
    ## Step 4 ------------------------------------------------------------------------------------------------------
                    d = max(dist)
        ## Step 5 ---------------------------------------------------------------------------------------------------h---
                    if d > 1:
                        try:
                            T = [ i for i in range(vertices) if dist[i] == d - 1 ]
                            all_cc_counts = components_count(vertices=T, graph=H)
                            if all_the_same(all_cc_counts):
                                degree_T = calculate_degrees_list(indexList=T, graph=H)
                                if all_the_same(degree_T):
                                    init = min(T)                                   # vertex with minimum label
                                else:
                                    index = degree_T.index(max(degree_T))           # vertex with maximum degree
                                    init = T[index]
                            else:
                                index = all_cc_counts.index(min(all_cc_counts))     # vertex with minimum connectec component
                                init = T[index]
                        except (ValueError, TypeError):
                            return 'Try angain please!'
                        S.append(init)
        # --------------------------------------------------------------------------------------------------------------
        ## Step 6 ------------------------------------------------------------------------------------------------------
                    elif d == 1:
                        H = generate_H(graph=graph, S=S)
                        is_disjoint, components = connectedComponents(graph=H)
                        if is_disjoint != 1:
                            return S
                        else:
                            try:
                                degree_H = calculate_degrees(graph=H)
                                if all_the_same(degree_H):
                                    init = min(L)
                                else:
                                    init = degree_H.index(max(degree_H))
                                S.append(init)
                            except (ValueError, TypeError):
                                return 'Try angain please!'        
        # --------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    return S