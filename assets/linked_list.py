

class Node2:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node2(data)
            return

        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node2(data)

    def get_all(self):
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current.next_node
        return data_list
    
    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next_node
        return length
