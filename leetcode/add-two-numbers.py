# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def parse_int(head):
    n = 0
    multiplier = 1
    curr = head
    while curr:
        n += curr.val * multiplier
        multiplier *= 10
        curr = curr.next
    return n


def build_linked_list(list_values):
    if not list_values:
        return None

    # values are in reverse order, so just pop from end
    head = ListNode(list_values.pop())
    curr = head
    while list_values:
        n = ListNode(list_values.pop())
        curr.next = n
        curr = n

    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = parse_int(l1), parse_int(l2)

        if n1 == 0:
            return l2
        if n2 == 0:
            return l1

        values = [int(c) for c in (str(n1+n2))]
        return build_linked_list(values)

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        tail = result
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, val = divmod(v1+v2+carry, 10)

            tail.next = ListNode(val)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
