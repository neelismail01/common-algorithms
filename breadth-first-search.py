### format of graph provided to function
### graph = {
###   'A' = ['B', 'C'],
###   'B' = ['A', 'E', 'G']
###   'C' = ...
### }


def breadthFirstSearch(graph, node, visited = []):
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited
