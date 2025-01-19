from src.LinkedList import LinkedList
from src.LinkedList import find_kth_from_end

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

def test_reverse_01():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    expected = "(1)->(2)->(3)"
    assert str(ll) == expected
    ll.reverse()
    expected = "(3)->(2)->(1)"
    assert str(ll) == expected

def test_get_middle_node_01():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    ll.append('E')
    assert str(ll.get_middle_node()) == '(C)'

def test_get_middle_node_02():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    assert str(ll.get_middle_node()) == '(C)'

def test_has_loop_01():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    ll.tail.next = ll.head.next.next # create loop
    assert ll.has_loop()


def test_has_loop_02():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    assert not ll.has_loop()

def test_find_kth_from_end_01():
    ll = LinkedList()
    assert find_kth_from_end(ll, 0) is None
    assert find_kth_from_end(ll, 1) is None
    assert find_kth_from_end(ll, 2) is None

def test_find_kth_from_end_02():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    assert find_kth_from_end(ll, 4).value is 'A'

def test_find_kth_from_end_03():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    assert find_kth_from_end(ll, 1).value is 'D'

def test_find_kth_from_end_04():
    ll = LinkedList('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    assert find_kth_from_end(ll, 99) is None


def test_partition_list_01():
    # Normal Case
    x = 3
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    assert str(ll) == "(3)->(1)->(4)->(2)->(5)"
    ll.partition_list(x)
    assert str(ll) == "(1)->(2)->(3)->(4)->(5)"

def test_partition_list_02():
    # All Equal Values
    x = 3
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    assert str(ll) == "(3)->(3)->(3)"
    ll.partition_list(x)
    assert str(ll) == "(3)->(3)->(3)"
    
def test_partition_list_03():
    # Single Element
    x = 3
    ll = LinkedList(1)
    assert str(ll) == "(1)"
    ll.partition_list(x)
    assert str(ll) == "(1)"

def test_partition_list_04():
    # Already Sorted
    x = 2
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "(1)->(2)->(3)"
    ll.partition_list(x)
    assert str(ll) == "(1)->(2)->(3)"

def test_partition_list_05():
    # Reverse Sorted
    x = 2
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    assert str(ll) == "(3)->(2)->(1)"
    ll.partition_list(x)
    assert str(ll) == "(1)->(3)->(2)"

def test_partition_list_06():
    # All Smaller Values
    x = 2
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    assert str(ll) == "(1)->(1)->(1)"
    ll.partition_list(x)
    assert str(ll) == "(1)->(1)->(1)"


def test_partition_list_07():
    # Single Element, Equal to Partition
    x = 3
    ll = LinkedList(3)
    assert str(ll) == "(3)"
    ll.partition_list(x)
    assert str(ll) == "(3)"