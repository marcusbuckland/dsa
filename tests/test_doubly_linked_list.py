from src.DoublyLinkedList import DoublyLinkedList

def test_dll_constuctor_01():
    dll = DoublyLinkedList()
    assert str(dll) == ""

def test_dll_constuctor_02():
    dll = DoublyLinkedList('A')
    assert str(dll) == ('(A)')