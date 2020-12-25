from vertex_cover import *
from standard_input import generate_random_graph
import time

if __name__ == "__main__":
    node = 100
    edge = 4500
    
    init = 0
    graph = generate_random_graph(node=node, edge=edge)

    start_time = time.time()
    VC = compute_vertex_cover(init=init , graph=graph)
    end_time = time.time()

    ## PRINT OUTPUTS ----------------------------------------------
    print("Number Of Node: ", node, "\nNumber Of Egde: ", edge, "\nTime: ",end_time - start_time, "\n----------------------------")
    print("The Vertex Cover: ", VC, "\nNumber Of Vertex-Cover Node:", len(VC))