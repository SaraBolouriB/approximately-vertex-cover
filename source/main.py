from vertex_cover import *
from dijkstra import *
from component import *

def compute_vertex_cover(init, graph):
    vertices = len(graph[0])
    ## Step 1 ----------------------------------------------------------
    S, L, T, dist, isolated_v = []    
    S.append(init-1)
    #-------------------------------------------------------------------

    ## H = graph - S
    H = generate_H(H=graph, S=S)  

    ## whether all vertices of H are isolated or not.                  
    is_isolated, isolated_verticex = isolated_vertex(H)

    while not is_isolated:

        ## Find Leafage
        leafages = find_leafage(graph=H)
        if len(leafages) != 0:
            for l in leafages:
                parent_node = H[l].index(1)
                S.append(parent_node)
        else:
            L = generate_L(G=graph, S=S, iso_set=isolated_verticex)
            dist = dijkstra(source=init-1, graph=H, graphL=L)
            d = max(dist)
            if d > 1:
                d -= 1
                T = [ i for i in range(vertices) if dist[i] == d]
                all_cc_counts = list()
                for vertex in T:
                    new_graph = generate_H(H=H, S=vertex)
                    cc_count = connectedComponents(graph=new_graph)
                    all_cc_counts.append(cc_count)
                if all_the_same(all_cc_counts):
                    degree_T = calculate_degree(graph=T)
                    if all_the_same(degree_T):
                        newVertex = min(T) # vertex with minimum label
                    else:
                        newVertex = max(degree_T) # vertex with maximum degree
                else:
                    newVertex = all_cc_counts.index(min(all_cc_counts)) # vertex with minimum connectec component
                    
                S.append = newVertex
            elif d == 1:
                pass

        H = generate_H(H=graph, S=S)
        is_isolated, isolated_verticex = isolated_vertex(H)

    print(S)


def all_the_same(elements):
   if len(elements) < 1:
       return True
   return len(elements) == elements.count(elements[0])