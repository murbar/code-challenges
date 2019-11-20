def reverse(head):
    previous = None
    current = head
    following = head

    while current != None:
        following = following.next
        current.next = previous
        previous = current
        current = following

    return previous
