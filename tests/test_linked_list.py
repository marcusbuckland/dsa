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

def test_pop_01():
    ll = LinkedList()
    ll.append(1)
    node = ll.pop()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0
    assert node.value == 1

def test_pop_02():
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    node = ll.pop() # 9
    assert ll.head.value == 1
    assert ll.tail.value == 8
    assert ll.length == 8
    assert node.value == 9
    node = ll.pop() # 8
    node = ll.pop() # 7
    node = ll.pop() # 6
    node = ll.pop() # 5
    assert ll.head.value == 1
    assert ll.tail.value == 4
    assert ll.length == 4
    assert node.value == 5
