import sys

def dijkstra(source, graph, graphL, lenG):
    '''
        Find the shortes path in "graph" from "source"
        1. Find number of vertices
        2. initial source vertex to 0   
        3. initial other vertices to MAXSIZE
    '''
    graphL.append(source)
    dist = [sys.maxsize] * lenG
    dist[source] = 0
    watchedVertices = [False] * lenG
    for i in range(lenG):
        watchedVertices[i] = None if i not in graphL else False
    for v in range(lenG):
        if v in graphL:
            min = minDistance(dist, watchedVertices, lenG)
            watchedVertices[min] = True

            nodes = graph[min]
            for u in nodes:
                if watchedVertices[u] == False:
                    if dist[min] + 1 < dist[u]:
                        dist[u] = dist[min] + 1
        elif v is not source:
            dist[v] = -1
    return dist
    
def minDistance(dist, watchedVertices, numV):
    min = sys.maxsize
    index = -1
    for v in range(numV):
        if dist[v] < min and watchedVertices[v] == False:
            min = dist[v]
            index = v
    
    return index