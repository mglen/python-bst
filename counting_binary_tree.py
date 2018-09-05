import binary_tree


class BinaryTree(binary_tree.BinaryTree):

    def size(self):
        return 1 + self.root.count_descendants()


class Node(binary_tree.Node):

    def __init__(self):
        super(Node, self).__init__()
        self.descendants = 0

    def count_descendants(self):
        """Return count of nodes below the current node.

        Time complexity is O(1).
        """
        return self.descendants

    def _add(self, value):
        # This is not optimal, but I wanted to keep building on the
        # existing code. It would be more efficient to replace the _add
        # method entirely.
        super(Node, self)._add(value)
        self._recalculate_descendants()

    def _recalculate_descendants(self):
        result = 0
        if self.left:
            result += 1 + self.left.descendants
        if self.right:
            result += 1 + self.right.descendants
        self.descendants = result

