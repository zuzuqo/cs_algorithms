import unittest

from binary_search import binary_search_recursive, binary_search
from bfs import bfs
from dfs import dfs, dfs_max_deep, dfs_child_parent, dfs_parent_child


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.TestBinarySearch = binary_search
        self.TestBinarySearchRecursive = binary_search_recursive
        self.array = [-34, 0, 1, 9, 48, 96, 345, 1000]

    def test_binary_search(self):
        self.assertEqual(self.TestBinarySearch(self.array, -8), None)
        self.assertEqual(self.TestBinarySearch(self.array, -34), 0)
        self.assertNotEqual(self.TestBinarySearch(self.array, 9), None)

    def test_binary_search_recursive(self):
        self.assertEqual(self.TestBinarySearchRecursive(self.array, -8, 0, len(self.array) - 1), None)
        self.assertEqual(self.TestBinarySearchRecursive(self.array, -34, 0, len(self.array) - 1), 0)
        self.assertNotEqual(self.TestBinarySearchRecursive(self.array, -34, 0, len(self.array) - 1), None)


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.TestBFS = bfs
        self.graph = {'A': ['B', 'C'],
                      'B': ['D', 'E'],
                      'C': ['F'],
                      'D': [],
                      'E': ['F'],
                      'F': []
                      }

    def test_bfs(self):
        self.assertEqual(self.TestBFS(self.graph, 'A'), 'A B C D E F')
        self.assertNotEqual(self.TestBFS(self.graph, 'A'), None)
        self.assertEqual(self.TestBFS(self.graph, 'B'), 'B D E F')
        self.assertNotEqual(self.TestBFS(self.graph, 'B'), 'B C D E F')


class TestDFS(unittest.TestCase):
    def setUp(self):
        self.TestDFS = dfs
        self.TestDFSMaxDeep = dfs_max_deep
        self.TestDFSChildParent = dfs_child_parent
        self.TestDFSParentChild = dfs_parent_child

        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        self.flipped_graph = {
            'A': [],
            'B': ['A'],
            'C': ['A'],
            'D': ['B', 'C']
        }

    def test_dfs(self):
        self.assertEqual(self.TestDFS(self.graph, 'A'), ['A', 'B', 'D', 'E', 'F', 'C'])

    def test_dfs_max_deep(self):
        self.assertEqual(self.TestDFSMaxDeep(self.graph, 'A'), 4)

    def test_dfs_child_parent(self):
        self.assertEqual(self.TestDFSChildParent(self.flipped_graph, 'A', 'D'), True)

    def test_dfs_parent_child(self):
        self.assertEqual(self.TestDFSParentChild(self.graph, 'A', 'C'), True)


if __name__ == '__main__':
    unittest.main()
