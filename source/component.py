def DFS(source, graph, visited, temp):
    temp.append(source)
    vertices = len(graph[source])
    
    visited[source] = True
    for v in range(vertices):
        if graph[source][v] == 1 and visited[v] == False:
            temp = DFS(v, graph, visited, temp)
    return temp

def connectedComponents(graph):
    vNumber = len(graph[0])
    visited = [False for i in range(vNumber)]
    cc = []

    for v in range(vNumber):
        if visited[v] == False:
            temp = []
            cc.append(DFS(v, graph, visited, temp))

    return len(cc)