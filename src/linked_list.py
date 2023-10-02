class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            new_node.next_node = self.head
            self.head = self.tail = new_node
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self):
        """Метод возвращает список данных односвязного списка"""
        total_list = []
        node = self.head
        while node:
            total_list.append(node.data)
            node = node.next_node
        return total_list

    def get_data_by_id(self, value):
        """Метод возвращает элемент из списка данных односвязного списка,
        если элемент типа dict и у него есть ключ 'id',
        иначе обрабатывает raise TypeError и выводит сообщение."""
        data = self.to_list()
        for item in data:
            try:
                if not isinstance(item, dict):
                    raise TypeError
                elif item.get('id') == value:
                    return item
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
