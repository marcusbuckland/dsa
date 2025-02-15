from src.DoublyLinkedList import DoublyLinkedList

def test_constuctor_01():
    dll = DoublyLinkedList()
    assert str(dll) == ""

def test_constuctor_02():
    dll = DoublyLinkedList('A')
    assert str(dll) == ('(A)')

def test_str_01():
    dll = DoublyLinkedList()
    assert str(dll) is ""

def test_str_02():
    dll = DoublyLinkedList('ABC')
    assert str(dll) == "(ABC)"

def test_str_03():
    dll = DoublyLinkedList(1)
    dll.append(2)
    assert str(dll) == "(1)<->(2)"

def test_append_01():
    dll = DoublyLinkedList()
    dll.append(1)
    assert dll.head.value == 1
    assert dll.tail.value == 1
    assert dll.head.next is None
    assert dll.tail.next is None
    assert dll.head.prev is None
    assert dll.head.prev is None
    assert dll.length == 1

def test_append_02():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.prev is None
    assert dll.tail.value == 2
    assert dll.tail.next is None
    assert dll.tail.prev.value == 1
    assert dll.length == 2

def test_append_03():
    dll = DoublyLinkedList()
    for i in range(1, 10):
        dll.append(i)
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.prev is None
    assert dll.tail.value == 9
    assert dll.tail.next is None
    assert dll.tail.prev.value is 8
    assert dll.length == 9

def test_pop_01():
    dll = DoublyLinkedList()
    assert dll.length == 0
    assert dll.pop() is None
    assert dll.pop() is None
    assert dll.length == 0


def test_pop_02():
    dll = DoublyLinkedList()
    dll.append(1)
    node = dll.pop()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0
    assert node.value == 1

def test_pop_03():
    dll = DoublyLinkedList()
    for i in range(1, 10):
        dll.append(i)
    node = dll.pop() # 9
    assert node.value == 9

    assert dll.head.value == 1
    assert dll.head.prev is None
    assert dll.head.next.value == 2
    assert dll.tail.value == 8
    assert dll.tail.prev.value == 7
    assert dll.tail.next is None
    assert dll.length == 8

    node = dll.pop() # 8
    assert node.value == 8
    assert dll.length == 7

    node = dll.pop() # 7
    assert node.value == 7
    assert dll.length == 6

    node = dll.pop() # 6
    assert node.value == 6
    assert dll.length == 5

    node = dll.pop() # 5
    assert node.value == 5
    assert dll.length == 4

    assert dll.head.value == 1
    assert dll.head.prev is None
    assert dll.head.next.value == 2
    assert dll.tail.value == 4
    assert dll.tail.next is None
    assert dll.tail.prev.value is 3
    assert dll.length == 4

def test_prepend_01():
    dll = DoublyLinkedList()
    dll.prepend(1)
    assert dll.head.value == 1
    assert dll.tail.value == 1
    assert dll.head.next is None
    assert dll.head.prev is None
    assert dll.tail.next is None
    assert dll.tail.prev is None
    assert dll.length == 1

def test_prepend_02():
    dll = DoublyLinkedList()
    dll.append(2)
    dll.append(3)
    dll.prepend(1)
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.prev is None
    assert dll.tail.value == 3
    assert dll.tail.next is None
    assert dll.tail.prev.value == 2
    assert dll.length == 3

def test_pop_first_01():
    # Empty DLL
    dll = DoublyLinkedList()
    node = dll.pop_first()
    assert node is None
    assert dll.length == 0

def test_pop_first_02():
    # DLL with 1 node
    dll = DoublyLinkedList(1)
    dll.append(2)
    node = dll.pop_first()
    assert node.value == 1
    assert dll.length == 1
    assert dll.head.next is None
    assert dll.head.prev is None

def test_pop_first_03():
    # DLL with 2+ nodes
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    node = dll.pop_first()
    assert node.value == 1
    assert dll.length == 3
    assert dll.head.value == 2
    assert dll.head.next.value == 3
    assert dll.head.prev is None
    node = dll.pop_first()
    assert node.value == 2
    assert dll.length == 2
    assert dll.head.value == 3
    assert dll.head.next.value == 4
