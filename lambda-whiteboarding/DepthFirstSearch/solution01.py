def recursive(node, cb):
    cb(node.value)

    if node.left:
        recursive(node.left, cb)

    if node.right:
        recursive(node.right, cb)

def iterative(node, cb):
    queue = []

    queue.append(node)

    while len(queue) > 0:
        next = queue.pop()

        if next.left:
            queue.append(next.left)

        if next.right:
            queue.append(next.left)

        cb(next.value)

    