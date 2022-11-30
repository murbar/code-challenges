# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1 -> 2 -> 4, 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode("dummy")
        final = current  # return final.next

        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return final.next


# debug helpers

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
    s = Solution()
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    assert read_list(s.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]
