# https://leetcode.com/problems/palindrome-linked-list/

# first intuition is to read values into an array and check the array
# more efficient way invloves 2 pointers, fast and slow
# when the fast pointer reaches the end of the list, the slow will be at the middle
# reverse list from slow to end
# check values of both "sublists", from head to middle, and reversed list from end to middle
# values should be equal at each node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse(head):
    preceding = None
    while head:
        following = head.next
        head.next = preceding
        preceding = head
        head = following

    return preceding


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow now points to middle element
        last_half = reverse(slow)
        # first_half = head

        # last_half is our list reversed starting at end and going to middle
        while last_half:
            if last_half.val != head.val:
                return False
            last_half = last_half.next
            head = head.next

        return True
