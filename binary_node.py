
class Node:
    """Node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def count_descendants(self):
        """Return count of nodes below the current node.
        
        Time complexity: O(n)
        Space complexity: O(1) best case, O(tree_depth) worst case
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

