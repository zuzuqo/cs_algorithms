# Depth First Search (DFS) - алгоритм обхода графа в глубину
# Берет верхний элемент и добавляет его в список посещенных
# Создает список смежных узлов этой вершины
# Добавляет те, которых нет в списке посещенных
# Повторяет все шаги, пока не обойдет всё


def dfs(graph, start, visited=[]):
    '''
    Standart Depth First Search (DFS) Algorithm
    :param graph:   data
    :param start:   data element
    :param visited: list of visited items
    :return:        list of visited items in visited order
    '''
    if start not in visited:
        visited.append(start)
        print(start, end=' ')
        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)
    return visited


def dfs_parent_child(graph, start, stop, visited=[]):
    '''
    Whether the start element is the parent of the stop element
    :param graph:   data
    :param start:   data element
    :param stop:    data element
    :param visited: list of visited items
    :return:        Bool
    '''
    if start not in visited:
        visited.append(start)
        for neigbor in graph[start]:
            if neigbor == stop:
                return True
            dfs_parent_child(graph, neigbor, stop, visited)
    return False


# for this function the graph must be flipped
def dfs_child_parent(graph, child, parent, visited=[]):
    '''
    Whether the initial element is a child of the parent element
    :param graph:   data
    :param child:   data element
    :param parent:  data element
    :param visited: list of visited items
    :return:        Bool
    '''
    if child not in visited:
        visited.append(child)
        for neigbor in graph[child]:
            if neigbor == parent:
                return True
            dfs_child_parent(graph, neigbor, parent, visited)
    return False


def dfs_max_deep(graph, start, visited=[]):
    '''
    Max graph depth
    :param graph:   data
    :param start:   data element
    :param visited: list of visited items
    :return:        max graph depth
    '''
    c = 1
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            c = max(c, dfs_max_deep(graph, neighbor, visited)+1)
    return c


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')
print()
print(dfs_parent_child(graph, 'A', 'C'))

# for this function the graph must be flipped
graph2 = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C']
}
print(dfs_child_parent(graph2, 'D', 'A'))

print(dfs_max_deep(graph, 'A'))
