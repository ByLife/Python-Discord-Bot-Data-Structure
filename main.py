class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __ne__(self, other):
        return self.data != other.data
    
    def __lt__(self, other):
        return self.data < other.data
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __repr__(self):
        return str(self.head)
    
    def __str__(self):
        return str(self.head)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current
            self.current = self.current.next
            return data
    
    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError
        else:
            current = self.head
            for i in range(index):
                current = current.next
            current.data = value
    
    def __delitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            self.length -= 1
    
    def __contains__(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError
        else:
            new_list = LinkedList()
            current = self.head
            while current is not None:
                new_list.append(current.data)
                current = current.next
            current = other.head
            while current is not None:
                new_list.append(current.data)
                current = current.next
            return new_list
    
    def __iadd__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError
        else:
            current = other.head
            while current is not None:
                self.append(current.data)
                current = current.next
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def insert(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length:
            raise IndexError
        elif index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.length += 1
        
    def remove(self, data):
        if self.head is None:
            raise IndexError
        elif self.head.data == data:
            self.head = self.head.next
            self.length -= 1
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    self.length -= 1
                    break
                current = current.next

    def sort(self):
        if self.head is None:
            raise IndexError
        else:
            current = self.head
            while current is not None:
                next = current.next
                while next is not None:
                    if current.data > next.data:
                        temp = current.data
                        current.data = next.data
                        next.data = temp
                    next = next.next
                current = current.next
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

class Stack:
    def __init__(self):
        self.stack = LinkedList()
    
    def __repr__(self):
        return str(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
    
    def __iter__(self):
        return iter(self.stack)
    
    def __next__(self):
        return next(self.stack)
    
    def __getitem__(self, index):
        return self.stack[index]
    
    def __setitem__(self, index, value):
        self.stack[index] = value
    
    def __delitem__(self, index):
        del self.stack[index]
    
    def __contains__(self, item):
        return item in self.stack
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

#Make a new chained list
my_list = LinkedList()

#Add some nodes
my_list.append(1)
my_list.append(6)
my_list.append(10)
my_list.append(4)
my_list.append(5)

#Print the length of the list
print(len(my_list), end='\n\n')

#Print the first node
print(my_list[0])

my_list.sort()

my_list.print()