class BinaryTree:
  def __init__(self, left, right, val):
    self.left = left
    self.right = right
    self.val = val

small_tree = BinaryTree(BinaryTree(None,None,3), BinaryTree(None,None,2), 1)
larger_tree = BinaryTree(BinaryTree(None,None,4), small_tree, 5)

# Write a function tree_max() that takes a binary tree as an argument and returns the largest value in the tree.
# Should consider the value of None branches to be negative infinity, float('-inf')
# This function should be recursive.

# First version
def tree_max(tree):
    if tree == None:
        return float('-inf')
    if tree.left == None and tree.right == None:
        return tree.val
    return max(tree.val, tree_max(tree.left), tree_max(tree.right))


# Second version
def tree_max(tree):
    if tree is None:
        return float('-inf')
    return max(tree.val, tree_max(tree.left), tree_max(tree.right))


