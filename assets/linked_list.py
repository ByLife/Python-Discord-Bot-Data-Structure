class Node:
    def __init__(self, question=None, next_node=None, yes_node=None, no_node=None):
        self.question = question
        self.next_node = next_node
        self.yes_node = yes_node
        self.no_node = no_node


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

class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    def get_length(self):
        length = 0
        for item in self.map:
            if item is not None:
                length += 1
        return length
    
    def get_all(self):
        data_list = []
        for item in self.map:
            if item is not None:
                data_list.append(item)
        return data_list
    
    def is_empty(self):
        return self.get_length() == 0
    
    def clear(self):
        self.map = [None] * self.size