"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue

queue = Queue()


class TestQueue(unittest.TestCase):

    def test_queue_enqueue(self):
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEquals(queue.head.data, 'data1')
        self.assertEquals(queue.head.next_node.data, 'data2')
        self.assertEquals(queue.tail.data, 'data3')
        with self.assertRaises(AttributeError):
            queue.tail.next_node.data

    def test_queue_dequeue(self):
        queue.enqueue('data1')
        queue.enqueue('data2')

        self.assertEquals(queue.dequeue(), 'data1')
        self.assertEquals(queue.dequeue(), 'data2')
        self.assertEquals(queue.dequeue(), None)
