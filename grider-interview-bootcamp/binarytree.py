# binary trees afford efficient searching
# left child is usually less than parent
# right child is usually greater


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if self.value == value:
            return self

        if value < self.value and self.left:
            return self.left.find(value)
        elif self.right:
            return self.right.find(value)

        return None

    def __str__(self):
        return str(self.value)

# tree traversal algorithms
# Depth first (left before right, pre: root first, post: root last)
#   (for binary trees)
#   inorder (left, root, right)
#   preorder (root, left, right)
#   postorder (left, right, root)
# Breath first (level order)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value)


def printPreorder(root):
    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)


def print_tree(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(n) for n in current_level))
        next_level = []
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level


n = BinaryTreeNode(10)
n.insert(15)
n.insert(1)
n.insert(8)
n.insert(20)
n.insert(12)
n.insert(7)

# print_tree(n)
assert n.find(20).value == 20
assert not n.find(25)
assert not n.find(-5)
assert n.find(8).value == 8
