# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.node = ListNode(0)
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.node
        curr_index = 0
        while curr.next:
            curr = curr.next
            if curr_index == index:
                return curr.val
            curr_index += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.node.next)
        curr = self.node
        self.node.next = new_node
        self.count += 1
        return None

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.node
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.count += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return -1
        curr = self.node
        new_node = ListNode(val)

        curr_index = -1
        while curr:
            if curr_index == index - 1:
                new_node.next = curr.next
                curr.next = new_node
                self.count += 1
                return None
            curr = curr.next
            curr_index += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        curr = self.node
        print(self.count)
        if index < 0 or self.count - 1 < index:
            return None

        curr_index = -1
        while curr:
            if curr_index == index - 1:
                curr.next = curr.next.next
                self.count -= 1
                # curr.next.next = None
                return None
            curr = curr.next
            curr_index += 1
        return None

    def __str__(self):
        curr = self.node.next
        result = ''
        while curr:
            result += str(curr.val) + '-->'
            curr = curr.next
        return result


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# for i in range(1,5):
#     obj.addAtHead(i)

# # for k in range(100, 90, -1):
# #     obj.addAtTail(k)
# obj.deleteAtIndex(1)

# print(obj)
# for j in range(100):
#     print(obj.get(j))  # prints 9 8 7 6 5
#     obj.get(j)



# test=["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# test1=[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
# test=["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
# test1=[[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
# obj1=MyLinkedList()
# k=0
# for i in test:
#     print(i,test1[k],k,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     if i == "MyLinkedList":
#         obj1=MyLinkedList()
#     if i == "addAtHead":
#         obj1.addAtHead(test1[k][0])
#         print(obj1,f"addAtHead {test1[k][0]}")
#     if i == "deleteAtIndex":
#         print(obj1,f"deleteAtIndex {test1[k][0]}")
#         obj1.deleteAtIndex(test1[k][0])
#         print(obj1)
#     if i == "addAtTail":
#         obj1.addAtTail(test1[k][0])
#         print(obj1,f"addAtTail {test1[k][0]}")
#     if i == "addAtIndex":
#         obj1.addAtIndex(test1[k][0],test1[k][1])
#         print(obj1,f"addAtIndex {test1[k][0],test1[k][1]}")
#     if i == "get":
#         print(obj1.get(test1[k][0]))
#     k+=1
# print(obj1)

