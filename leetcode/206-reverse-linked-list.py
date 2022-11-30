# https://leetcode.com/problems/reverse-linked-list/

# three pointers: one for the current node, one ofr previous, one for next
# move pointers in specific order to reverse list
# for each node
#   record its current next
#   change its next to the node that pointed to it
#   move to next node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # preceding is new end of list, None/null
        preceding = None
        current = head
        following = head

        while current != None:
            # keep reference to next node
            following = following.next
            # point current node to previous node
            current.next = preceding
            # set previous node to current for next iteration
            preceding = current
            # process next node
            current = following

        return preceding

    def reverseList2(self, head: ListNode) -> ListNode:
        # simplified, fewer variables
        preceding = None
        while head:
            # pattern here is a chain of assignments:
            # follwing -> head.next -> preceding -> head -> following
            following = head.next
            head.next = preceding
            preceding = head
            head = following

        return preceding
