class Node:
    def __init__(self, question=None, next_node=None, yes_node=None, no_node=None):
        self.question = question
        self.next_node = next_node
        self.yes_node = yes_node
        self.no_node = no_node
