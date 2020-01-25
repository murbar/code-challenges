# https://leetcode.com/problems/sort-list/

# simliar to "merge two sorted lists"
# break the list in half and sort each half
# list is sorted when it has one node
# then merge the sorted lists into one, recursively


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge(self, l1, l2):
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

    def split(self, head):
        mid = tail = cut = head
        while tail and tail.next:
            cut = mid
            mid = mid.next
            tail = tail.next.next
        # mid points to middle element, cut is element preceding mid
        # cut list in half, head -> cut & slow -> tail
        cut.next = None
        return head, mid

    def sortList(self, head: ListNode) -> ListNode:
        # null list, or list length 1
        if not head or not head.next:
            return head

        head, mid = self.split(head)
        # careful to capture return values here to pass to merge
        # if not, left and right point to nodes other than head after lists are sorted
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)


# testing helpers

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


values = [-5, 4, 2, 1, 5, 3, 0, 8]
ll = build_list(values)
s = Solution()
s.sortList(ll)
assert read_list(ll) == sorted(values)
