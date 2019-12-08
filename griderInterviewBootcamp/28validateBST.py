# given root, validate that every node's left child is less than parent, and right
# child is greater than
'''
node may be valid but maybe not when compared to parent

        10
      /    \
     8     12
   /  \
  7   15
'''
# keep track of min and max, update at each level recursively

from binarytree import BinaryTreeNode


def validate(root, low_limit=None, high_limit=None):
    if high_limit is not None and root.value >= high_limit:
        return False

    if low_limit is not None and root.value < low_limit:
        return False

    if root.left and not validate(root.left, low_limit, root.value):
        return False

    if root.right and not validate(root.right, root.value, high_limit):
        return False

    return True


n = BinaryTreeNode(10)
n.insert(15)
n.insert(1)
n.insert(8)
n.insert(20)
n.insert(12)
n.insert(7)

assert validate(n)
twenty = n.find(20)
# 5 is less than root of 10, but is on the right side of tree
twenty.insert(5)
# tree now invalid
assert not validate(n)
print('All tests passed!')
