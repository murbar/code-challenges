# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# split array in half around middle element
# add left half to left of middle element, right to right, recursively


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        # if nums is length one, left and right will be empty lists
        # if length 2, right will be empty
        mid = len(nums) // 2
        left, root, right = nums[:mid], nums[mid], nums[mid+1:]
        tree = TreeNode(root)
        tree.left = self.sortedArrayToBST(left)
        tree.right = self.sortedArrayToBST(right)
        return tree
