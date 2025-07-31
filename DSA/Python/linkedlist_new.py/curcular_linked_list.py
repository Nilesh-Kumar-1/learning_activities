# let starts with linkefed list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node # update tail to new node
        self.length += 1
    def prepend(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
    def insert(self,data,index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
    def search(self, data):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                return False
    def get(self, index):
        if (index < 0 or index >= self.length or not self.head) and not reverse:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    def set_value(self, index, data):
        if index < 0 or index >= self.length or not self.head:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data
    def pop_first(self):
        if not self.head:
            raise IndexError("List is empty")
        elif self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return
        current = self.head
        self.head = self.head.next
        self.tail.next = self.head
        self.length -= 1
        return current.data
    def pop_last(self):
        if not self.head:
            raise IndexError("List is empty")
        elif self.length == 1:
            current = self.head
            self.head = self.tail = None
            self.length = 0
            return current.data
        current = self.head
        while current.next != self.tail:
            current = current.next
        popped_data = self.tail.data
        self.tail = current
        self.tail.next = self.head
        self.length -= 1
        return popped_data
    def remove(self, index):
        if index < 0 or index >= self.length or not self.head:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop_last()
        current = self.head
        for _  in range(index - 1):
            current = current.next
        removed_data = current.next.data
        current.next = current.next.next
        self.length -= 1
        return removed_data
    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while True:
            result.append(f"{current.data} -->")
            current = current.next
            if current == self.head:
                result.append(f"{self.head.data} (head)")
                break
        return "".join(result) 
    
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
    def __str__(self):
        return str(self.data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        if not self.head:
            return False
        if data < self.head.data:
            self.prepend(data)
            return
        elif data > self.tail.data:
            self.append(data)
            return
        curr = self.head
        while curr.next.data > data:
            curr = curr.next
            if curr == self.head:
                return
        new_node = Node(data)
        new_node.next = curr.next.next
        curr.next = new_node
        return
    def __str__(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while True:
            result.append(f"{current.data} -->")
            current = current.next
            if current == self.head:
                result.append(f"{self.head.data} (head)")
                break
        return "".join(result) 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        if not self.head:
            return False
        if data < self.head.data:
            self.prepend(data)
            return
        curr = self.head
        # print(curr.data)
        while data > curr.next.data:
            if curr.next == self.head:
                self.append(data)
                return
            curr = curr.next
            # print(curr.data)
        # print(self)   
        print(curr.data, curr.next.data)
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
        return
    def __str__(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while True:
            result.append(f"{current.data} -->")
            current = current.next
            if current == self.head:
                result.append(f"{self.head.data} (head)")
                break
        return "".join(result) 

sol = CircularLinkedList()
for i in range(5):
    sol.append(1 * i)
sol.append(10)  # Append 0 to the end
# sol.delete_by_value(4)
print(sol)
sol.insert_into_sorted(-1) # Output: True
# print(sol)  # Output: -1 -->0 -->1 -->2 -->3 -->4 -->-1 (head)
sol.insert_into_sorted(50)  # Output: True
print(sol)  # Output: -1 -->0 -->1 -->2 -->3 -->4 -->5 -->-1 (head)
sol.insert_into_sorted(6)  # Output: True
sol.insert_into_sorted(7)  # Output: True
sol.insert_into_sorted(8)  # Output: True
print(sol)  # Output: -1 -->0 -->1 -->2 -->2 -->3 -->4 -->5 -->-1 (head)
#     # print(sol)  # Output: 0 -->1 -->2 -->3 -->4 -->0 -->
# # print(sol.print_list())  # Output: 0 -->1 -->2 -->3 -->4 -->0 -->
# print(sol.length)  # Output: 5
# print(sol)  # Output: 0

# for i in range(-1,-10,-1):
#     sol.prepend(i)
# print(sol)  # Output: -1 -->-2 -->-3 -->-4 -->-5 -->0 -->1 -->2 -->3 -->4 -->0 (head)

# sol.set_value(0, 100)

# print(sol)
# sol.append(0)
# sol.pop_first()
# # print(sol.pop_last())
# sol.prepend(-2)
# print(sol.pop_last())  # Output: -2 -->0 (head)
# print(sol)  # Output: -2 -->-3 -->-4 -->-5 -->0 -->1 -->2 -->3 -->4 -->-2 (head)

# for i in range(5):
#     sol.append(1 * i)
# print(sol)  # Output: -2 -->-3 -->-4 -->-5 -->0 -->1 -->2 -->3 -->4 -->-2 (head)
# for i in range(5):
#     print(sol.pop_last(), sol.length)
# print(sol)  # Output: -2 -->-3 -->-4 -->-5 -->0 (head)



