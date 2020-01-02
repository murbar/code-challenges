# https://leetcode.com/problems/intersection-of-two-linked-lists/

# no. 1
# implement k from last function
# get last nodes
# if last nodes differ, no intersection
# else increment k until nodes differ
# return last shared node
# O(1) space
# O(n^2) time

# no. 2
# use hash set to store each node in list A
# iterate over list B, if node is in set, return as intersection
# O(m+n) space, O(mn)

# no. 3
# use two pointers for current nodes of A and B
# when current reaches end of list, redirect to head of other list
# if intersection exists, current will point to same node eventually
# eg. A = {1,3,5,7,9,11}, B = {2,4,9,11}, intersection at 9
# at 5 iterations A will point to 9, B to start of A (1)
# after 4 more iterations A will point to 9 in B, B will point to 9 in A
# A == B so return either as intersection node
# if both pointers reach their end and end nodes do not match, no intersection exists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def k_from_last(ll, k):
    if not ll or k < 0:
        return None

    kth, end = ll, ll

    for _ in range(k):
        if not end.next:
            # k is larger than length of list
            return None
        end = end.next

    while end.next:
        end = end.next
        kth = kth.next

    return kth

# tests

# a = ListNode('a')
# b = ListNode('b')
# c = ListNode('c')
# d = ListNode('d')
# e = ListNode('e')
# a.next = b
# b.next = c
# c.next = d
# d.next = e

# assert k_from_last(a, 3).val == 'b'
# assert k_from_last(a, 0).val == 'e'
# assert k_from_last(a, 4).val == 'a'
# assert k_from_last(a, 5) == None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # quadratic running time, O(1) space
        if not headA or not headB:
            return None

        a_last = k_from_last(headA, 0)
        b_last = k_from_last(headB, 0)

        # lists will always share last node if intersection exists
        if a_last is not b_last:
            return None

        # step back through both lists and move intersection node back until nodes diverge
        i = 1
        intersect_node = a_last
        while True:
            a_kth = k_from_last(headA, i)
            b_kth = k_from_last(headB, i)
            if a_kth and b_kth and a_kth is b_kth:
                intersect_node = a_kth
                i += 1
            else:
                # i is greater than length of either list or nodes have diverged
                break

        return intersect_node

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        # use hash set, linear running time, O(n) or O(m) space
        if not headA or not headB:
            return None

        a_nodes = set()

        a_current = headA
        while a_current:
            a_nodes.add(a_current)
            a_current = a_current.next

        b_current = headB
        while b_current:
            if b_current in a_nodes:
                return b_current
            else:
                b_current = b_current.next

        return None

    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode:
        # the most clever and performant solution but also the least intuitive
        # same principle as finding a cycle in a single list
        # (iterate two pointers at different speeds until they converge)
        # linear time, constant space

        if not headA or not headB:
            return None

        a_current = headA
        b_current = headB

        a_end = None
        b_end = None

        while True:
            if a_end and b_end and a_end is not b_end:
                return None

            if a_current is b_current:
                return a_current

            if a_current.next:
                a_current = a_current.next
            else:
                a_end = a_current
                a_current = headB

            if b_current.next:
                b_current = b_current.next
            else:
                b_end = b_current
                b_current = headA
