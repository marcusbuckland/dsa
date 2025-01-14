class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"({self.value})"
        
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

    def __str__(self):
        temp = self.head
        l = []
        while temp is not None:
            l.append(f"({temp.value})->")
            temp = temp.next
        l.append(f"{self.tail.next}")
        return "".join(l)

    def print_list(self):
        temp = self.head
        l = []
        while temp is not None:
            l.append(f"({temp.value})->")
            temp = temp.next
        print("".join(l))

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

    def get_node(self, index):
        """ Get the node at the given index 
        Args:
            index (int): Index of the node to get"""
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_node(self, index, value):
        """ Set the value of the node at the given index 
        Args:
            index (int): Index of the node to set
            value (int): Value to set"""
        temp = self.get_node(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length :
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length :
            return self.append(value)
        
        node = Node(value)
        temp = self.get_node(index-1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length :
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length:
            return self.pop()
        
        prev = self.get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head # reverse head & tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def get_middle_node(self):
        # Note- Implementation cannot use self.length
        slow = self.head
        fast = self.head

        while fast is not None and fast != self.tail:
            slow = slow.next
            fast = fast.next.next

        return slow

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast : return True
        
        return False