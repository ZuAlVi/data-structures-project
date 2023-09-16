"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack

stack = Stack()


class TestStack(unittest.TestCase):

    def test_Stack_Push(self):
        stack.push('data1')
        stack.push('data2')
        self.assertEquals(stack.top.data, 'data2')
        self.assertEquals(stack.top.next_node.data, 'data1')
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.data
