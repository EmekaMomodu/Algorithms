"""

  The distance between a node in a Binary Tree and the tree's root is called the
  node's depth.


  Write a function that takes in a Binary Tree and returns the sum of its nodes'
  depths.

"""


def nodeDepths(root, depth=0):
    if root is None:
        return 0

    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
