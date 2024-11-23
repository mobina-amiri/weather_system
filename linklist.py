class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._head = None

    def insert(self, data):
        new_node = self.Node(data)
        new_node.next = self._head
        self._head = new_node

    def remove(self, data):
        current = self._head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self._head = current.next
                return
            prev = current
            current = current.next

    def __iter__(self):  # این متد LinkedList را قابل پیمایش می‌کند
        current = self._head
        while current:
            yield current.data
            current = current.next
