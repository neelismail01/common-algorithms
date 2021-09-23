def depthFirstSearch(graph, node, visited = []):
    visited.append(node)
    for child in graph[node]:
        depthFirstSearch(graph, child, visited)
    return visited