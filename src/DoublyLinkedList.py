class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"({self.value})"
    
class DoublyLinkedList:
    def __init__(self, value=None):
        if value:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def __str__(self):
        temp = self.head
        l = []
        while temp:
            l.append(f"({temp.value})")
            temp = temp.next
        return "<->".join(l)

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True
