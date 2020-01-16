from typing import List

'''
     DFS                 DFS                  DFS                 BFS
 Post-order           Pre-order             In-order           Level-order
Bottom -> Top       Top -> Bottom    Left -> Root -> Right    Left -> Right
Left -> Right       Left -> Right                             Top -> Bottom

      5                   1                    4                   1
     / \                 / \                  / \                 / \
    3   4               2   5                2   5               2   3
   / \                 / \                  / \                 / \
  1   2               3   4                1   3               4   5


Binary search tree in-order traversal returns values ordered smallest to largest
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# notice, due to nature of stack we add nodes in reverse order
# eg. pre-order (root-left-right) is added right-left-root


def in_order_traversal(root: TreeNode) -> List[int]:
    stack = [root]
    res = []
    while stack:
        current = stack.pop()
        if current:
            if isinstance(current, TreeNode):
                stack.append(current.right)
                stack.append(current.val)
                stack.append(current.left)
            else:
                res.append(current)
    return res


def post_order_traversal(root: TreeNode) -> List[int]:
    stack = [root]
    res = []
    while stack:
        current = stack.pop()
        if current:
            if isinstance(current, TreeNode):
                stack.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
            else:
                res.append(current)
    return res


def pre_order_traversal(root: TreeNode) -> List[int]:
    stack = [root]
    res = []
    while stack:
        current = stack.pop()
        if current:
            if isinstance(current, TreeNode):
                stack.append(current.right)
                stack.append(current.left)
                stack.append(current.val)
            else:
                res.append(current)
    return res


# can be done with a flag too, like this:
def pre_order_traversal2(root: TreeNode) -> List[int]:
    # is this item on the stack a node or a value?
    # (is_node, node/value)
    stack = [(True, root)]
    res = []
    while stack:
        is_node, current = stack.pop()
        if current:
            if is_node:
                stack.append((True, current.right))
                stack.append((True, current.left))
                stack.append((False, current.val))
            else:
                res.append(current)
    return res


# BFS with queue
def bf_traversal(root: TreeNode) -> List[int]:
    queue = [root]
    res = []
    while queue:
        current = queue.pop(0)
        if current:
            if isinstance(current, TreeNode):
                queue.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                res.append(current)
    return res


# tests
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.right = TreeNode(3)
l = TreeNode(2)
l.left = TreeNode(4)
l.right = TreeNode(5)
root.left = l

assert in_order_traversal(root) == [4, 2, 5, 1, 3]
assert post_order_traversal(root) == [4, 5, 2, 3, 1]
assert pre_order_traversal(root) == [1, 2, 4, 5, 3]
assert pre_order_traversal2(root) == [1, 2, 4, 5, 3]
assert bf_traversal(root) == [1, 2, 3, 4, 5]
