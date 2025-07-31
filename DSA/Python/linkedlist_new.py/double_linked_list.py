from operator import ne


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.data)
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    def __str__(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return " <-> ".join(map(str, result))
    def prepend(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    def transverse(self):
        if not self.head:
            return None
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    def reverse_transverse(self):
        if not self.tail:
            return None
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - index):
                current = current.prev
        return current.data if current else None
    def setValue(self,index, data):
        if not (0 <= index < self.length) or not self.head:
            return False
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - index):
                current = current.prev
        current.data = data
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length or not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        self.length -= 1
        return True
    def remove_by_value(self, data):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.data == data:
                if self.length == 1:
                    self.remove_all()
                    return True
                if current == self.head:
                    self.remove(0)
                    return True
                elif current == self.tail:
                    self.remove(self.length - 1)
                    return True
                current.prev.next = current.next 
            current = current.next
    def insert(self, data, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(data)
            return True
        elif index == self.length:
            self.append(data)
            return True
        new_node = Node(data)
        current = self.head
        for i in range(index-1):
            current = current.next
        temp = current.next
        current.next = new_node
        new_node.next = temp
        new_node.prev = current
        temp.prev = new_node
        self.length += 1
        return True
    def insert_into_sorted(self, data):
        if not self.head or self.head.data >= data:
            self.prepend(data)
            return True
        if self.tail.data <= data:
            self.append(data)
            return True
        current = self.head
        
        while current.data < data:
            current = current.next
        
        new_node = Node(data)
        temp = current.prev
        current.prev = new_node
        new_node.prev = temp
        new_node.next = current
        temp.next = new_node
        self.length += 1
        return True
    def pop_first(self):
        pass
    def pop_last(self):
        pass
    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0
sol = DoubleLinkedList()
for i in range(5):
    sol.append(i)
for i in range(6, 10):
    sol.append(i)
print(sol)
sol.remove_by_value(4)
print(sol)
# sol.remove_by_value(9)
# print(sol)
# sol.remove_by_value(0)
# print(sol)
# sol.remove_by_value(10)
# print(sol)
# sol = DoubleLinkedList()
# sol.remove_by_value(10)  # Should not raise an error
sol.insert_into_sorted(18)
print(sol) 
sol.insert_into_sorted(1.5)
print(sol) 
sol.insert_into_sorted(5.5)
print(sol) 
sol.insert_into_sorted(6.5)
print(sol)  # Should print "List is empty"