# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_(NLR)

# iterative in-order traversal of a binary tree
# left -> root -> right
# gonna need a stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # O(n) time/space

        values = []

        if not root:
            return values

        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            values.append(current.val)
            current = current.right

        return values

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # O(n) time/space
        # use helper function to simplify while loop

        values = []

        if not root:
            return values

        def add_left_to_stack(stack, node):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        add_left_to_stack(stack, root)
        while stack:
            current = stack.pop()
            values.append(current.val)
            if current.right:
                add_left_to_stack(stack, current.right)

        return values

    def inorderTraversalR(self, root: TreeNode) -> List[int]:
        # recursive, O(n) time/space

        def in_order(root, values):
            if root:
                in_order(root.left, values)
                values.append(root.val)
                in_order(root.right, values)

        values = []
        in_order(root, values)
        return values


# just for reference

def preorder_traversal(root):
    # root -> left -> right
    values = []

    if not root:
        return values

    stack = []
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return values


def preorder_traversal_recursive(root):
    # root -> left -> right
    def pre_order(root, values):
        if root:
            values.append(root.val)
            pre_order(root.left, values)
            pre_order(root.right, values)

    values = []
    pre_order(root, values)
    return values


def postorder_traversal(root):
    # left -> right -> root
    # perform pre-order, then reverse the result list
    # if we were only printing the values, this would use
    # unnecessary space for the values array (need it so we can reverse it at end)
    values = []

    if not root:
        return values

    stack = []
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return values[::-1]


def postorder_traversal_recursive(root):
    # left -> right -> root
    def post_order(root, values):
        if root:
            post_order(root.left, values)
            post_order(root.right, values)
            values.append(root.val)

    values = []
    post_order(root, values)
    return values
