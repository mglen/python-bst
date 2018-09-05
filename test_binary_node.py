import unittest
from binary_node import Node

class TestBinaryTree(unittest.TestCase):

    def test_single_node(self):
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.count_descendants(), 0)

    def test_single_child(self):
        node = Node(1)
        node.left = Node(0)
        self.assertEqual(node.count_descendants(), 1)

    def test_deep_structure(self):
        node = Node(1)
        node.left = Node(0)
        node.right = Node(2)
        node.right.right = Node(4)
        node.right.left = Node(3)
        self.assertEqual(node.count_descendants(), 4)

