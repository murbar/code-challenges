
def _get_path(root, value):
    if not root:
        return None

    # base case
    if root.value == value:
        return [root]

    # is value in the left subtree?
    left_path = _get_path(root.left, value)
    if left_path:
        left_path.append(root)
        return left_path

    # if not, is it in the right subtree?
    right_path = _get_path(root.right, value)
    if right_path:
        right_path.append(root)
        return right_path

    # value isn't in the tree
    return None


def lowest_common_ancestor(root, j, k):
    path_to_j = _get_path(root, j)
    path_to_k = _get_path(root, k)

    if not path_to_j or not path_to_k:
        return None

    lca = None
    for i in range(min(len(path_to_j), len(path_to_k))):
        if path_to_j[i] == path_to_k[i]:
            lca = path_to_j[i]
        else:
            break

    return lca


print('All tests passed!')
