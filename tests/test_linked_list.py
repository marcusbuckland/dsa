from src.LinkedList import LinkedList

def test_append_01():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.head.next is None
    assert ll.tail.next is None
    assert ll.length == 1

def test_append_02():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.tail.value == 2
    assert ll.tail.next is None
    assert ll.length == 2

def test_append_03():
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.tail.value == 9
    assert ll.tail.next is None
    assert ll.length == 9