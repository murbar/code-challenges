# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

'''
given preorder and in-order traversals of a tree, construct the binary tree
assume no duplicates in tree
pre-order implies preorder[0] is root
find value of preorder[0] in inorder array
left sub-tree values will be any values in inorder array to the left of the root
values to the right are in the right sub-tree
recur on sub-arrays to build the full tree

        1
       / \
      2   3
     / \   \
    4   5   6
           / \
          7   8
           \
            9
                        L        R
                       -------  -------------
pre (root, L, R)    1  2  4  5  3  6  7  9  8
                    ^
                    root

                     L           R
                    -------     -------------
in (L, root, R)     4  2  5  1  3  7  9  6  8
                             ^
                             root
'''

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# we need a recursive helper that tracks all of the required indexes
class Solution:
    def build(self, preorder, inorder, pre_start, pre_end, in_start, in_end):
        if pre_start > len(preorder) - 1 or in_start > in_end:
            return None

        rootValue = preorder[pre_start]
        root = TreeNode(rootValue)
        i = inorder.index(rootValue)

        left_start = pre_start + 1
        root.left = self.build(
            preorder, inorder, left_start, i, in_start, i-1)
        right_start = pre_start + i + 1 - in_start
        root.right = self.build(
            preorder, inorder, right_start, pre_end, i+1, in_end)

        return root

    def buildTree(self, preorder, inorder):
        return self.build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)


# less complex and more intuitive but the popping and slicing makes this solution
# slower and more memory intensive
# we could reverse preorder to avoid popping from the start of the list, or use a deque
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # any values left to process?
        if not inorder:
            return None

        # remove root from front of preorder list
        root_val = preorder.pop(0)
        # locate index of root in inorder list
        root_i = inorder.index(root_val)
        root = TreeNode(root_val)
        # left subtree will be built first
        root.left = self.buildTree(preorder, inorder[:root_i])
        # when we get to the right subtree, all of the left roots will
        # have been removed from the front of the preorder list
        root.right = self.buildTree(preorder, inorder[root_i+1:])
        return root
