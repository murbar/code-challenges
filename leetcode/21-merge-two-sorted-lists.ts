/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 *
 * We need three pointers that we will manipulate to build a new list.
 * O(N) time, # of node in both lists
 * O(1) space
 * Recursive: O(N) space
 */

// from my Python solution, building a new list
var mergeTwoLists = function (list1, list2) {
  let current = { val: 'dummy', next: null };
  let final = current;

  while (list1 !== null && list2 !== null) {
    if (list1.val > list2.val) {
      current.next = list2;
      list2 = list2.next;
    } else {
      current.next = list1;
      list1 = list1.next;
    }
    current = current.next;
  }

  if (list1 !== null) {
    current.next = list1;
  }

  if (list2 !== null) {
    current.next = list2;
  }

  return final.next;
};

// from AlgoExpert, mutating list1
var mergeTwoListsAlt = function (list1, list2) {
  if (list1 === null) {
    return list2;
  }
  if (list2 === null) {
    return list1;
  }
  let prev = null;
  let curr1 = list1;
  let curr2 = list2;

  while (curr1 !== null && curr2 !== null) {
    if (curr1.val < curr2.val) {
      prev = curr1;
      curr1 = curr1.next;
    } else {
      if (prev !== null) {
        prev.next = curr2;
      }
      prev = curr2;
      curr2 = curr2.next;
      prev.next = curr1;
    }
  }

  if (curr1 === null) {
    prev.next = curr2;
  }

  return list1.val < list2.val ? list1 : list2;
};

// from AlgoExpert
var mergeTwoListsRecursive = function (list1, list2) {
  if (list1 === null) {
    return list2;
  }
  if (list2 === null) {
    return list1;
  }

  function merge(p1, p2, prev) {
    if (p1 === null) {
      prev.next = p2;
      return;
    }

    if (p2 === null) return;

    if (p1.val < p2.val) {
      merge(p1.next, p2, p1);
    } else {
      if (prev !== null) {
        prev.next = p2;
      }
      const newP2 = p2.next;
      p2.next = p1;
      merge(p1, newP2, p2);
    }
  }

  merge(list1, list2, null);
  return list1.val < list2.val ? list1 : list2;
};
