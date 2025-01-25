from src.DoublyLinkedList import DoublyLinkedList

def test_constuctor_01():
    dll = DoublyLinkedList()
    assert str(dll) == ""

def test_constuctor_02():
    dll = DoublyLinkedList('A')
    assert str(dll) == ('(A)')

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