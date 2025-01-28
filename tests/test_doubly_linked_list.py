from src.DoublyLinkedList import DoublyLinkedList

def test_constuctor_01():
    ddll = DoublyLinkedList()
    assert str(ddll) == ""

def test_constuctor_02():
    ddll = DoublyLinkedList('A')
    assert str(ddll) == ('(A)')

def test_str_01():
    ddll = DoublyLinkedList()
    assert str(ddll) is ""

def test_str_02():
    ddll = DoublyLinkedList('ABC')
    assert str(ddll) == "(ABC)"

def test_str_03():
    ddll = DoublyLinkedList(1)
    ddll.append(2)
    assert str(ddll) == "(1)<->(2)"

def test_append_01():
    ddll = DoublyLinkedList()
    ddll.append(1)
    assert ddll.head.value == 1
    assert ddll.tail.value == 1
    assert ddll.head.next is None
    assert ddll.tail.next is None
    assert ddll.head.prev is None
    assert ddll.head.prev is None
    assert ddll.length == 1

def test_append_02():
    ddll = DoublyLinkedList()
    ddll.append(1)
    ddll.append(2)
    assert ddll.head.value == 1
    assert ddll.head.next.value == 2
    assert ddll.head.prev is None
    assert ddll.tail.value == 2
    assert ddll.tail.next is None
    assert ddll.tail.prev.value == 1
    assert ddll.length == 2

def test_append_03():
    ddll = DoublyLinkedList()
    for i in range(1, 10):
        ddll.append(i)
    assert ddll.head.value == 1
    assert ddll.head.next.value == 2
    assert ddll.head.prev is None
    assert ddll.tail.value == 9
    assert ddll.tail.next is None
    assert ddll.tail.prev.value is 8
    assert ddll.length == 9

def test_pop_01():
    ddll = DoublyLinkedList()
    assert ddll.length == 0
    assert ddll.pop() is None
    assert ddll.pop() is None
    assert ddll.length == 0


def test_pop_02():
    ddll = DoublyLinkedList()
    ddll.append(1)
    node = ddll.pop()
    assert ddll.head is None
    assert ddll.tail is None
    assert ddll.length == 0
    assert node.value == 1

def test_pop_03():
    ddll = DoublyLinkedList()
    for i in range(1, 10):
        ddll.append(i)
    node = ddll.pop() # 9
    assert node.value == 9

    assert ddll.head.value == 1
    assert ddll.head.prev is None
    assert ddll.head.next.value == 2
    assert ddll.tail.value == 8
    assert ddll.tail.prev.value == 7
    assert ddll.tail.next is None
    assert ddll.length == 8

    node = ddll.pop() # 8
    assert node.value == 8
    assert ddll.length == 7

    node = ddll.pop() # 7
    assert node.value == 7
    assert ddll.length == 6

    node = ddll.pop() # 6
    assert node.value == 6
    assert ddll.length == 5

    node = ddll.pop() # 5
    assert node.value == 5
    assert ddll.length == 4

    assert ddll.head.value == 1
    assert ddll.head.prev is None
    assert ddll.head.next.value == 2
    assert ddll.tail.value == 4
    assert ddll.tail.next is None
    assert ddll.tail.prev.value is 3
    assert ddll.length == 4

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