from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# notice, due to nature of stack we add nodes in reverse order
# eg. pre-order (root-left-right) is added right-left-root


def in_order_traversal(self, root: TreeNode) -> List[int]:
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


def post_order_traversal(self, root: TreeNode) -> List[int]:
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


def pre_order_traversal(self, root: TreeNode) -> List[int]:
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
def pre_order_traversal2(self, root: TreeNode) -> List[int]:
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
