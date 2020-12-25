from vertex_cover_methods import generate_H

def DFS(source, graph, visited, temp):
    temp.append(source)
    vertices = graph[source]
    visited[source] = True
    for v in vertices:
        if visited[v] == False:
            temp = DFS(v, graph, visited, temp)
    return temp

def connectedComponents(graph, lenG):
    visited = [False for i in range(lenG)]
    cc = []

    for v in range(lenG):
        if graph[v]:
            if visited[v] == False and graph[v][0] != -1:
                temp = []
                result = DFS(v, graph, visited, temp)
                if len(result) > 1:
                    cc.append(result)
    return len(cc), cc

def components_count(vertices, graph, lenG):
    counts = []
    for vertex in vertices:
        new_graph = generate_H(graph=graph, S=[vertex], lenG=lenG)
        cc_count, cc = connectedComponents(graph=new_graph, lenG=lenG)
        counts.append(cc_count)

    return counts