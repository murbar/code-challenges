/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

type ListNode = {
    val: number;
    next: ListNode | null;
};

const reverseList = function (head: ListNode) {
    let preceding = null;
    while (head !== null) {
        let following = head.next;
        head.next = preceding;
        preceding = head;
        head = following;
    }
    return preceding;
};

// written with co-pilot
function reverseLinkedList(head) {
    let current = head;
    let previous = null;
    while (current !== null) {
        let next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
}

