/*
Remove Kth Linked List Node
Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list. 

For example, if we have the following linked list: 

(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).  

So after the function executes, the state of the linked list should be:

(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null. 

If k is longer than the length of the linked list, the linked list should not be changed. 

The optimal solution exhibits a runtime complexity of O(n) and a space complexity of O(1).
*/

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insertNode(value) {
    const newNode = new Node(value);
    if (this.head === null) {
      this.head = newNode;
    } else {
      let currentNode = this.head;
      let previousNode = null;
      while (currentNode !== null) {
        previousNode = currentNode;
        currentNode = currentNode.next;
      }
      previousNode.next = newNode;
    }
  }

  printNodes() {
    if (this.head === null) {
      console.log('Empty list');
    } else {
      const values = [];
      let currentNode = this.head;
      while (currentNode !== null) {
        values.push(currentNode.value);
        currentNode = currentNode.next;
      }
      console.log(values.join(' -> '));
    }
  }
}

function removeKthLinkedListNode(head, k) {
  let currentNode = head;
  let listLength = 0;
  const lastKNodes = [];
  while (currentNode !== null) {
    listLength++;
    lastKNodes.push(currentNode);
    if (listLength > k + 1) {
      lastKNodes.shift();
    }
    currentNode = currentNode.next;
  }

  if (lastKNodes.length < k || k === 0) {
    return head;
  } else if (lastKNodes.length === k) {
    return lastKNodes[1];
  } else if (k === 1) {
    lastKNodes[0].next = null;
    return head;
  } else {
    lastKNodes[0].next = lastKNodes[2];
    return head;
  }
}

const values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11];

const LL = new LinkedList();
values.forEach(v => LL.insertNode(v));
LL.printNodes();

const newHead = removeKthLinkedListNode(LL.head, 0);
LL.head = newHead;
LL.printNodes();
