# determine if a linked list is circular ("last" node points to a node earlier in the list)
# causes infinate loops in a lot of LL logic

# use two pointers

from llist import LinkedList


def is_circular(llist):
    slow, fast = llist.head, llist.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


l = LinkedList()
for i in range(950):
    l.insert_first(f'node {i}')
assert is_circular(l) == False
end = l.get_last()
node = l.get(300)
end.next = node
assert is_circular(l)
print('All tests passed!')
