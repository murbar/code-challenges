# return middle node of linked list
# if size is even, return node at end of first half of list
# solve by only iterating over the list once

# use two pointers - slow & fast
# increment slow by 1, fast by 2
# when fast reaches end of list, slow should reference the middle element

from llist import LinkedList


def midpoint(llist):
    mid, end = llist.head, llist.head

    while end.next and end.next.next:
        mid = mid.next
        end = end.next.next

    return mid


l = LinkedList()
for i in range(9):
    l.insert_first(f'node {i}')
# middle is 'node 4'
assert midpoint(l).data == 'node 4'
l.insert_first('another node')
# size is now odd
assert midpoint(l).data == 'node 5'
print('All tests passed!')
