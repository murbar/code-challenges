# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# validate binary search tree
# track high and low value limits through recursive calls
# init limits to null, check left and right sub trees with limits set to root's value
# O(n) time/space, each node visited once, call stack up to n deep

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low_limit=None, high_limit=None):
            # this is not a node
            if not node:
                return True

            # high limit was set by parent node, is current val less than?
            if high_limit is not None and node.val >= high_limit:
                return False

            # low limit was set by parent node, is current val greater than?
            if low_limit is not None and node.val <= low_limit:
                return False

            # validate left subtree, pass current val as high limit
            # no elements in left subtree can have value greater than current node's value
            if not validate(node.left, low_limit, node.val):
                return False

            # validate right subtree, pass current val as low limit
            # no elements in right subtree can have value less than current node's value
            if not validate(node.right, node.val, high_limit):
                return False

            # all checks passed
            return True

        return validate(root)

    def isValidBST_iterative(self, root: TreeNode) -> bool:
        # iterative implementation with DFS, stack
        # O(n) time/space

        if not root:
            return True

        # store node, low limit, high limit
        stack = [(root, None, None)]
        while stack:
            node, low_limit, high_limit = stack.pop()

            if not node:
                continue

            if low_limit is not None and node.val <= low_limit:
                return False

            if high_limit is not None and node.val >= high_limit:
                return False

            stack.append((node.right, node.val, high_limit))
            stack.append((node.left, low_limit, node.val))

        return True

    def isValidBST_iterative2(self, root: TreeNode) -> bool:
        # iterative implementation with DFS, stack
        # use infinity for starting low/high

        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low_limit, high_limit = stack.pop()

            if not node:
                continue

            value = node.val
            if value <= low_limit or value >= high_limit:
                return False

            stack.append((node.right, value, high_limit))
            stack.append((node.left, low_limit, value))

        return True

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        # traverse tree in-order
        # Left -> Root -> Right
        # each element should be smaller than the one following
        # O(n) time/space

        stack = []
        last_value = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                # go left until we can't
                root = root.left
            root = stack.pop()
            # this element's value must be greater than the last value
            if root.val <= last_value:
                return False
            # set last value
            last_value = root.val
            # go right
            root = root.right

        return True
