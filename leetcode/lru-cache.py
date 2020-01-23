# https://leetcode.com/problems/lru-cache/

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# all ops in O(1) time
# list/dictionary combination? ordered dict?
# probably need a doubly-linked list to remove items from the middle in constant time


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        # dummy nodes simplify removing a node from the head or tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        '''Add node to head of list'''
        head_next = self.head.next
        head_next.prev = node
        self.head.next = node
        node.next = head_next
        node.prev = self.head

    def new_node(self, key, value):
        '''Create a new node and add to head of list'''
        node = ListNode(key, value)
        self.add(node)
        return node

    def remove(self, node):
        '''Remove a node from the list'''
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        return node

    def pop_last(self):
        '''Remove and return the last node in the list'''
        return self.remove(self.tail.prev)

    def move_to_head(self, node):
        '''Move a node to the head of the list'''
        self.remove(node)
        self.add(node)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item_map = {}
        self.item_list = LinkedList()

    def check_capacity(self):
        if len(self.item_map) == self.capacity:
            item = self.item_list.pop_last()
            del self.item_map[item.key]

    def get(self, key: int) -> int:
        node = self.item_map.get(key, None)
        if not node:
            return -1
        else:
            self.item_list.move_to_head(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        node = self.item_map.get(key, None)
        if node:
            node.value = value
            self.item_list.move_to_head(node)
        else:
            self.check_capacity()
            node = self.item_list.new_node(key, value)
            self.item_map[key] = node
