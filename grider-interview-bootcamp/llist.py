
class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def remove_first(self):
        if self.head:
            self.head = self.head.next

    def get_first(self):
        return self.head

    def get_last(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next
        return current

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def insert_last(self, data):
        last = self.get_last
        node = Node(data)
        if last:
            last.next = node
        else:
            self.head = node

    def get(self, index):
        i = 0
        current = self.head
        while current:
            if i == index:
                return current
            i += 1
            current = current.next

        return None

    def insert(self, index, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return node

        if index == 0:
            node.next = self.head
            self.head = node
            return node

        prev = self.get(index-1)
        if not prev:
            prev = self.get_last()
        node.next = prev.next
        prev.next = node
        return node

    def remove(self, index):
        target = self.get(index)
        if not target:
            return None

        if index == 0:
            self.head = self.head.next
            return target

        prev = self.get(index-1)
        prev.next = target.next
        return target

    def clear(self):
        self.head = None

    def __len__(self):
        s = 0
        current = self.head
        while current:
            s += 1
            current = current.next
        return s

    # makes the list iterable but does not make it an iterator, technically
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __getitem__(self, index):
        return self.get(index)


# l = LinkedList()
# n3 = Node('node 3')
# n2 = Node('node 2', n3)
# n1 = Node('node 1', n2)
# l.head = n1
# print(len(l))
# print(l[2].data)

# for el in l:
#     print(el.data)

# print([el.data for el in l])
