# Binary Search Tree

Simple example of a binary search tree, with a `count_descendants()` method on the Node object.

The `add()` method is recursive, so there is a node limit based on the Python stack size (and since
this is not a balanced BST, that limit could be 1000 nodes).
