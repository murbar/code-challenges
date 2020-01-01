from collections import deque

# DFS -> stack -> vertical
# BFS -> queue -> horizontal


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        c = TreeNode(data)
        self.children.append(c)

    def remove_child(self, data):
        # removes all children with matching data
        self.children = [c for c in self.children if c.data != data]


class Tree:
    def __init__(self, root=None):
        self.root = root

    def breath_traverse(self, op=None):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            queue.extend(node.children)
            if op:
                op(node)
            else:
                yield node

    def depth_traverse(self, op=None):
        if not self.root:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            if op:
                op(node)
            else:
                yield node


def print_node(node):
    print(node.data)


# n = TreeNode('root')
# for i in range(3):
#     n.add_child(f'node {i}')
# for c in n.children:
#     c.add_child(f'node {c.data} leaf 1')
#     c.add_child(f'node {c.data} leaf 2')

# tree = Tree(n)
# print('BF traverse:')
# tree.breath_traverse(print_node)
# print('DF traverse:')
# tree.depth_traverse(print_node)

# DF_nodes = [n.data for n in tree.breath_traverse()]
# print('DF nodes list: ', DF_nodes)
