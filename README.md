# Python Binary Trees

Simple examples of binary trees in python, see below for explanations of each. All code both
Python2 and Python3 compatible.


## `binary_node.py`

Defines a `Node` object implementing a `count_descendants()` method. A tree can be built
by manually assigning child nodes to `node.left` and `node.right`.

## `binary_tree.py`

Defines a `BinaryTree` object representing the root of a binary tree, and extends the `Node`
in `binary_node.py` to add ordered children.

The `add()` method is recursive, so there is a node limit based on the Python stack size (and since
this is not a balanced binary tree, that limit could be 1000 nodes).

# Testing

Run tests with:
```
python -m unittest
```

