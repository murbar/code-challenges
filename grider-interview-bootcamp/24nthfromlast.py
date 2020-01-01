# find the nth node from the last node in linked list
# assume n is less than length of list

# another two-pointer solution

from llist import LinkedList


def nth_from_end(ls, n):
    aft, forward = ls.head, ls.head

    for _ in range(n):
        forward = forward.next

    while forward.next:
        aft = aft.next
        forward = forward.next

    return aft


l = LinkedList()
for i in range(20):
    l.insert_first(f'node {i}')
# for el in l:
#     print(el.data)
assert nth_from_end(l, 5).data == 'node 5'
assert nth_from_end(l, 19).data == 'node 19'
assert nth_from_end(l, 1).data == 'node 1'
assert nth_from_end(l, 0).data == 'node 0'
print('All tests passed!')
