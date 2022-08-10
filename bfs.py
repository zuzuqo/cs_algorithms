# Breadth First Search (BFS) - алгоритм обхода графа в ширину
# Создаются списки посещенных элементов и очереди
# Первый элемент очереди добавляется в список посещенных
# Создается список смежных узлов этого элемента
# Добавляются элементы, отсутствующие в списке посещенных, в конец очереди
# И так, пока очередь не опустеет


def bfs(graph, node):
    '''
    Breadth First Search (BFS)
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


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'B')
bfs(graph, 'A')
