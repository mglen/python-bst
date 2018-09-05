
class Node:
    """Node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def count_descendants(self):
        """Return count of nodes below the current node."""
        pass

    def add(self, value):
        """Add a new node to the tree.
        
        Adding a node that already exists causes no change.
        """
        if value < self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

