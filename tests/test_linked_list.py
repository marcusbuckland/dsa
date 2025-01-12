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

def test_prepend_01():
    ll = LinkedList()
    ll.prepend(1)
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.head.next is None
    assert ll.tail.next is None
    assert ll.length == 1

def test_prepend_02():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.prepend(1)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.tail.value == 3
    assert ll.tail.next is None
    assert ll.length == 3

def test_pop_first_01():
    ll = LinkedList()
    ll.append(1)
    node = ll.pop_first()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0
    assert node.value == 1

def test_pop_first_02():
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    node = ll.pop_first() # 1
    assert ll.head.value == 2
    assert ll.tail.value == 9
    assert ll.length == 8
    assert node.value == 1
    node = ll.pop_first() # 2
    node = ll.pop_first() # 3
    node = ll.pop_first() # 4
    node = ll.pop_first() # 5
    assert ll.head.value == 6
    assert ll.tail.value == 9
    assert ll.length == 4
    assert node.value == 5

def test_get_node_01():
    ll = LinkedList()
    ll.append(1)
    assert ll.get_node(0).value == 1

def test_get_node_02():
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    assert ll.get_node(0).value == 1
    assert ll.get_node(1).value == 2
    assert ll.get_node(2).value == 3
    assert ll.get_node(3).value == 4
    assert ll.get_node(4).value == 5
    assert ll.get_node(5).value == 6
    assert ll.get_node(6).value == 7
    assert ll.get_node(7).value == 8
    assert ll.get_node(8).value == 9

def test_set_node_01():
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    ll.set_node(0, 100)
    ll.set_node(1, 200)
    ll.set_node(2, 300)
    assert ll.get_node(0).value == 100
    assert ll.get_node(1).value == 200
    assert ll.get_node(2).value == 300

def test_set_node_02():
    ll = LinkedList()
    ll.set_node(0, 100)
    assert ll.head is None

def test_insert_01():
    ll = LinkedList()
    ll.insert(0, 1)
    assert ll.head.value is 1
    assert ll.head.next is None

def test_insert_02():
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(5)
    ll.insert(1, 200)
    ll.insert(2, 300)
    assert ll.get_node(0).value == 1
    assert ll.get_node(1).value == 200
    assert ll.get_node(2).value == 300
    assert ll.get_node(3).value == 4
    assert ll.get_node(4).value == 5

def test_remove_01():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.remove(index=2)
    assert ll.length == 4
    node = ll.get_node(index=2)
    assert node.value == 4
