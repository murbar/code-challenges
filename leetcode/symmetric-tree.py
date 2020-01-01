# https://leetcode.com/problems/symmetric-tree/

'''
- if root is null, tree is symmetric
- recursive function needs to take two nodes for comparison
- base cases
    - if both nodes are null, tree is symmetric
    - if only one node is null, tree is not symmetric
    - if both nodes are not null, node must be equal
        - then both left and right subtrees must be symmetric (recursive call)
- key to recognize the base cases
- need a way to compare nodes
- if it were an array, we could do it with pairs of indexes
- O(n) time, O(h) space
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def checkSymmetric(left, right):
    # if either is null, they both must be
    if left == None or right == None:
        return left == right

    if left.val != right.val:
        return False

    return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return checkSymmetric(root.left, root.right)
