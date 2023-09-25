class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        temp = Node(data)
        if self.tail is None:
            self.head = self.tail = temp
        self.tail.next_node = temp
        self.tail = temp

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head.next_node is None:
            data = self.head.data
            self.head.data = None
            self.tail = None
        else:
            data = self.head.data
            self.head = self.head.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        return f'{self.head.data}\n{self.head.next_node.data}\n{self.tail.data}'

