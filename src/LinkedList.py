class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.head is None: # LinkedList is empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True
    
    def pop(self):
        # LinkedList is empty
        if self.length == 0 :
            return None
        
        # LinkedList contains one node only
        if self.length == 1 :
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        # LinkedList contains two or more nodes
        prev = self.head
        temp = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True
    
    def pop_first(self):
        # LinkedList is empty
        if self.length == 0 :
            return None
        
        # LinkedList contains one node only
        if self.length == 1 :
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        
        # LinkedList contains two or more nodes
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp