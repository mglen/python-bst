
class Node:
    """Node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def count_descendants(self):
        """Return count of nodes below the current node.
        
        Takes O(n) time and O(log n) space.
        """
        stack = [self]
        size = 0
        while stack:
            node = stack.pop()
            if node.right:
                size += 1
                stack.append(node.right)
            if node.left:
                size += 1
                stack.append(node.left)
        return size

