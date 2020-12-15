import sys
import numpy as np

def dijkstra(source, graph, graphL):
    '''
        Find the shortes path in "graph" from "source"
        1. Find number of vertices
        2. initial source vertex to 0   
        3. initial other vertices to MAXSIZE
    '''
    vertices = len(graph[0])
    dist = [sys.maxsize] * vertices
    dist[source] = 0
    watchedVertices = []
    for i in range(vertices):
        watchedVertices[i] = None if i not in graphL else False
        
    for v in range(vertices):
        if v in graphL:
            min = minDistance(dist, watchedVertices)
            watchedVertices[min] = True

            for u in range(vertices):
                if graph[min][u] > 0 and dist[u] == False:
                    if dist[min] + graph[min][u] < dist[u]:
                        dist[u] = dist[min] + graph[min][u]

    return dist
    
def minDistance(dist, watchedVertices):
    numV = len(dist)
    min = sys.maxsize

    for v in range(numV):
        if dist[v] < min and watchedVertices[v] == False:
            min = dist[v]
            index = v
    
    return index