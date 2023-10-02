"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_linked_list_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'data1': 1})
        ll.insert_beginning({'data2': 2})
        self.assertEquals(ll.head.data, {'data2': 2})
        self.assertEquals(ll.head.next_node.data, {'data1': 1})

    def test_linked_list_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'data1': 1})
        ll.insert_at_end({'data2': 2})
        self.assertEquals(ll.tail.data, {'data2': 2})
        self.assertEquals(ll.tail.next_node, None)

    def test_linked_list_str(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEquals(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_linked_list_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEquals(ll.to_list(), [
            {'id': 1, 'username': 'lazzy508509'},
            {'id': 2, 'username': 'mik.roz'},
        ])




