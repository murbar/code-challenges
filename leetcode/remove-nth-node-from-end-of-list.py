# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# two pointers
# increment fast pointer n times, then both until fast reached end
# slow is not at nth node, remove it
# what edge cases are there to consider?
# list contains one node -> null
# when target is first or last node


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # problem stated n will always be valid
        # we need a dummy node to point to our head
        stub = ListNode(0)
        stub.next = head
        # init two pointers at dummy node
        forward = stub
        rear = stub

        # move forward pointer ahead n+1 times
        # eg. n = 5, move 6 nodes so pointers are seperated by 5 nodes
        for _ in range(n+1):
            forward = forward.next

        # forward and rear now have n nodes between them
        # keep advancing both until forward hits end of list
        while forward:
            forward = forward.next
            rear = rear.next

        # rear next is now our target
        # rear may be the dummy node is head is the target
        rear.next = rear.next.next
        # return the new head
        return stub.next


# some helpers for testing


def build_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next

    return head


def read_list(head):
    if not head:
        return []

    values = [head.val]
    current = head

    while current.next:
        current = current.next
        values.append(current.val)

    return values


if __name__ == '__main__':

    # test helpers
    ls = [1, 5, 8, 0, 4]
    assert read_list(build_list(ls)) == ls

    cases = [
        (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
        (([1, 2, 3, 4, 5], 1), [1, 2, 3, 4]),
        (([1, 2, 3, 4, 5], 5), [2, 3, 4, 5]),
        (([8, 9], 2), [9]),
        (([8, 9], 1), [8]),
        (([8], 1), []),
    ]

    s = Solution()
    for args, expected in cases:
        ls, n = args
        actual = read_list(s.removeNthFromEnd(build_list(ls), n))
        if actual != expected:
            print(f'FAILED ({ls} {n}) -> {actual}, expected {expected}')
