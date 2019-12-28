# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if not root:
            return result

        q = []
        q.append(root)
        while len(q):
            curr_level = []
            for _ in range(len(q)):
                node = q.pop(0)
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(curr_level)

        return result
