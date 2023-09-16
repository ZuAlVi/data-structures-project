"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack

stack = Stack()
stack_2 = Stack()


class TestStack(unittest.TestCase):

    def test_stack_push(self):
        stack.push('data1')
        stack.push('data2')
        self.assertEquals(stack.top.data, 'data2')
        self.assertEquals(stack.top.next_node.data, 'data1')
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.data

    def test_stack_pop(self):
        stack_2.push('data1')
        self.assertEquals(stack_2.pop(), 'data1')
        self.assertIsNone(stack_2.top)
        stack_2.push('data1')
        stack_2.push('data2')
        self.assertEquals(stack_2.pop(), 'data2')
        self.assertEquals(stack_2.top.data, 'data1')
