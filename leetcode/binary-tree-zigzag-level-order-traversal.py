# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# BF traversal to get level order values
# flag to reverse every other level


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = [root]
        zag = False
        while len(queue):
            level = []
            # process all nodes that are in the stack right now
            # will not process nodes added inside of this loop
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # reverse values for every other level
            if zag:
                level = level.reverse()

            result.append(level)
            zag = not zag

        return result
