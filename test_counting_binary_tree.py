import unittest
from counting_binary_tree import BinaryTree


class TestNode(unittest.TestCase):

    def test_basic_tree(self):
        tree = BinaryTree(5)
        tree.add(4).add(8).add(6).add(7)

        self.assertEqual(tree.size(), 5)
        self.assertEqual(tree.root.right.count_descendants(), 2)

    def test_node_already_exists(self):
        tree = BinaryTree(50)
        tree.add(25)
        tree.add(25)

        self.assertEqual(tree.size(), 2)

    def test_deep_tree(self):
        tree = BinaryTree(0)
        for i in range(1, 500):
            tree.add(i)

        self.assertEqual(tree.size(), 500)
        self.assertEqual(tree.root.right.count_descendants(), 498)
