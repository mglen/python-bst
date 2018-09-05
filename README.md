# Python Binary Trees

Simple examples of binary trees in python, see below for explanations of each. All code is
Python2 and Python3 compatible.

## binary_node.py

Defines a `Node` class with a `count_descendants()` method. A tree can be built by manually
assigning child nodes to `node.left` and `node.right`.

## binary_tree.py

Extends binary_node.py by defining a `BinaryTree` class representing the root of a binary tree.
Includes an `add()` method to add ordered children.

The `add()` method is recursive, so tree depth is limited by the Python stack size (and since
this is not a balanced binary tree, that limit could be reached after 1000 nodes).

# Testing

Run tests with:
```
python -m unittest
```
