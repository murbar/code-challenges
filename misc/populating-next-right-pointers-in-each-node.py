# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        queue = []
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for i in range(len(level) - 1):
                level[i].next = level[i+1]

        return root

    def connect2(self, root: Node) -> Node:
        # we can populate the next pointer as we move through the level
        # the key difference is adding the child nodes in reverse order: right, then left
        # we move through the level from right to left
        # we can store the last node we've seen and point the next node's 'next' pointer to it
        if not root:
            return root

        queue = []
        queue.append(root)
        while queue:
            next_node = None
            for _ in range(len(queue)):
                node = queue.pop(0)

                if next_node:
                    node.next = next_node
                next_node = node

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return root
