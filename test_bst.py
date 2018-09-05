import unittest
from bst import Node

class TestNode(unittest.TestCase):

    def test_basic_tree(self):
        top = Node(50)
        top.add(25)
        top.add(75)
        top.add(100)
        top.add(99)

        self.assertEqual(top.value, 50)
        self.assertEqual(top.left.value, 25)
        self.assertEqual(top.right.value, 75)
        self.assertEqual(top.right.right.value,100)
        self.assertEqual(top.right.right.left.value,99)
        self.assertEqual(top.right.left, None)

    def test_node_already_exists(self):
        top = Node(50)
        top.add(25)
        top.add(25)
        self.assertEqual(top.left.value, 25)
        self.assertEqual(top.right, None)
        self.assertEqual(top.left.right, None)
        self.assertEqual(top.left.left, None)

