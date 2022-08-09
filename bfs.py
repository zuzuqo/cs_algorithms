# BFS (Breadth-First Search) - алгоритм обхода графа в ширину

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, node):
    '''
    BFS (Breadth-First Search)
    :param graph:   data
    :param node:    data element
    :return:        nested node elements
    '''
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()


bfs(graph, 'B')
bfs(graph, 'A')
