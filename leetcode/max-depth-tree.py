# https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''
- traverse the tree and keep track of each nodes depth as you go
- DF and BF traversals have the same performance, have to visit each node anyway
- O(n) time, O(h) space for DF, stack with be max size height of tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_depth = 1
        stack = [(root, 1)]
        while stack:
            current, depth = stack.pop()
            max_depth = max(depth, max_depth)

            if current.left:
                stack.append((current.left, depth+1))
            if current.right:
                stack.append((current.right, depth+1))

        return max_depth


# not my solution, elegant recursive alternative
def maxDepthR(root):
    if not root:
        return 0

    return 1 + max(maxDepthR(root.right), maxDepthR(root.left))


# max depth for n-ary tree
# add all children to stack in place of left/right
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
def maxDepthN(self, root: 'Node') -> int:
    if not root:
        return 0

    max_depth = 1
    stack = [(root, 1)]
    while stack:
        current, depth = stack.pop()
        max_depth = max(depth, max_depth)

        for c in current.children:
            stack.append((c, depth+1))

    return max_depth
