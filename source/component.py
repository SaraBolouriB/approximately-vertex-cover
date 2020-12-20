from vertex_cover_methods import generate_H

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
            result = DFS(v, graph, visited, temp)
            if len(result) > 1:
                cc.append(result)
    return len(cc), cc

def components_count(vertices, graph):
    counts = []
    for vertex in vertices:
        new_graph = generate_H(graph=graph, S=[vertex])
        cc_count, cc = connectedComponents(graph=new_graph)
        counts.append(cc_count)

    return counts