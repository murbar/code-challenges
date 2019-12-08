# given root of tree, return list where each element is width of the tree at each level
# width implies BF traversal

from collections import deque

from tree import TreeNode


def levelWidth(root):
    END = 'end of level'
    widths = [0]
    queue = deque([root, END])

    # END will remain after all nodes processed
    while len(queue) > 1:
        node = queue.popleft()

        if node is END:
            widths.append(0)
            queue.append(END)
        else:
            queue.extend(node.children)
            widths[-1] += 1

    return widths


n = TreeNode('root')
for i in range(3):
    n.add_child(f'node {i}')
for c in n.children:
    c.add_child(f'node {c.data} leaf 1')
    c.add_child(f'node {c.data} leaf 2')

assert levelWidth(n) == [1, 3, 6]
n.add_child('another child')
assert levelWidth(n) == [1, 4, 6]
print('All tests passed!')
