import binary_node

class BinaryTree:
    """Root of a binary tree."""

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """Add a new node to the tree.
        
        Adding a node that already exists causes no change
        to the tree.
        """
        self.root._add(value)
        return self

class Node(binary_node.Node):

    def _add(self, value):
        if value < self.value:
            if self.left:
                self.left._add(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right._add(value)
            else:
                self.right = Node(value)
