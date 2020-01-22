# https://leetcode.com/problems/copy-list-with-random-pointer/

# two-pass, duplicate list with random pointers as null
# build map of nodes Old -> New, use map to populate random pointers on second pass
# extra space required for map, size n

# better solution: modify original list
# interleave new nodes and old nodes o1-> n1 -> o2 -> n2
# odd nodes are original nodes, even are new nodes, old then new
# build links and then extract every other node for final list


class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return head

        # interleave new nodes following old nodes
        current = head
        while current:
            current.next = Node(current.val, current.next, None)
            # increment to next (old) node
            current = current.next.next

        # set random pointers
        current = head
        while current:
            # if random is null, do nothing
            if current.random:
                current.next.random = current.random.next
            # we've intereaved old with new, so we know there is an even number of nodes
            # no need to check next is null
            current = current.next.next

        # drop original nodes from list
        copy = head.next
        current = head
        while current.next:
            # capture current.next before we modify it
            n = current.next
            current.next = current.next.next
            current = n

        return copy


# using a map of old nodes -> new nodes
class Solution2:
    def copyRandomList(self, head):
        if not head:
            return head

        node_map = {}

        # clone list and populate map along the way
        copy = Node(head.val, None, None)
        current = head
        current_copy = copy

        node_map[current] = current_copy

        while current.next:
            current_copy.next = Node(current.next.val, None, None)
            current = current.next
            current_copy = current_copy.next
            node_map[current] = current_copy

        # copy the random pointers
        current = head
        current_copy = copy
        while current:
            if current.random:
                current_copy.random = node_map[current.random]
            current = current.next
            current_copy = current_copy.next

        return copy
