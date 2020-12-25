from dijkstra import *
from component import *
import random
from vertex_cover_methods import *

def compute_vertex_cover(init, graph):
    original_graph = tuple(map(tuple, graph))
    lenG = len(original_graph)                                              # Number of graph vertices 

    ## Step 1 ------------------------------------------------------------------------------------------------------
    # Initializing -------------------------------------------------------------------------------------------------
    S, Ss, L, T, dist, isolated_v = [], [], [], [], [], []
    is_disjoint, is_isolated = False, False
    S.append(init)                                                          # Add the first vertex to S
    # End initializing ---------------------------------------------------------------------------------------------

    while True:
        H = generate_H(graph=original_graph, S=S, lenG=lenG)                # Generate H = graph - S  
        is_isolated, isolated_v = is_isolated_graph(graph=H, lenG=lenG)     # Return check result and isolated vertices

        Ss.extend([iso for iso in isolated_v if iso not in Ss])             # Update Ss set

    ### End of the algorithm ### -----------------------------------------------------------------------------------
        if is_isolated:
            return S                                                        # Return vertex-cover set (S)
    ## Step 2 ------------------------------------------------------------------------------------------------------
        is_disjoint, components = connectedComponents(graph=H, lenG=lenG)   # Return check result and all components set

        if is_disjoint > 1:                                                 # if it is true, algorithm will be run for each component 
            for component in components:
                sub_G = sub_graph(vertices=component, graph=original_graph, lenG=lenG)
                vc = compute_vertex_cover(init=random.choice(component), graph=sub_G)
                S.extend(vc)
                Ss.extend(vc)
    
        else:
            leafages = find_leafage(graph=H, lenG=lenG)
            if len(leafages) != 0:
                parents = remove_parent(leafages=leafages, H=H)
                S.extend(parents)
                Ss.extend(parents)
    # --------------------------------------------------------------------------------------------------------------
    ## Step 3 ------------------------------------------------------------------------------------------------------
            else:
                L = generate_L(G=original_graph, S=S, iso_set=isolated_v, lenG=lenG)
                Hh = generate_H(graph=original_graph, S=Ss, lenG=lenG)       # calculated H without init

                if is_isolated_vertex(init, Hh):
                    degree_L = calculate_degrees_list(indexList=L, graph=H, lenG=lenG)
                    index = degree_L.index(max(degree_L))                    # vertex with maximum degree in L
                    init = L[index]
                    S.append(init)
                else:
                    Ss.append(init)
                    dist = dijkstra(source=init, graph=original_graph, graphL=L, lenG=lenG)
    # --------------------------------------------------------------------------------------------------------------
    ## Step 4 ------------------------------------------------------------------------------------------------------
                    d = max(dist)
        ## Step 5 --------------------------------------------------------------------------------------------------
                    if d > 1:
                        try:
                            T = [ i for i in range(lenG) if dist[i] == d - 1 ]
                            all_cc_counts = components_count(vertices=T, graph=H, lenG=lenG)
                            if all_the_same(all_cc_counts):
                                degree_T = calculate_degrees_list(indexList=T, graph=H, lenG=lenG)
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
                        H = generate_H(graph=graph, S=S, lenG=lenG)
                        is_disjoint, components = connectedComponents(graph=H, lenG=lenG)
                        if is_disjoint != 1:
                            for component in components:
                                sub_G = sub_graph(vertices=component, graph=original_graph)
                                vc = compute_vertex_cover(init=random.choice(component), original_graph=sub_G)
                                S.extend(vc)
                                Ss.extend(vc)
                        else:
                            try:
                                degree_H = calculate_degrees(graph=H, lenG=lenG)
                                if all_the_same(degree_H):
                                    init = min(L)
                                else:
                                    init = degree_H.index(max(degree_H))
                                S.append(init)
                            except (ValueError, TypeError):
                                return 'Try angain please!'        
        # --------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    return S