import unittest
from binary_tree import BinaryTree, Node


class TestNode(unittest.TestCase):

    def test_basic_tree(self):
        tree = BinaryTree(50)
        tree.add(25).add(75).add(100).add(99)

        root = tree.root
        self.assertEqual(root.value, 50)
        self.assertEqual(root.count_descendants(), 4)
        self.assertEqual(root.left.value, 25)
        self.assertEqual(root.right.value, 75)
        self.assertEqual(root.right.right.value, 100)
        self.assertEqual(root.right.right.left.value, 99)
        self.assertEqual(root.right.left, None)

    def test_node_already_exists(self):
        tree = BinaryTree(50)
        tree.add(25)
        tree.add(25)

        root = tree.root
        self.assertEqual(root.count_descendants(), 1)
        self.assertEqual(root.left.value, 25)
        self.assertEqual(root.right, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.left.left, None)

