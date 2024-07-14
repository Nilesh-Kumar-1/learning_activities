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
#Design a linked list
import random
class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self,cnt=0):
        self.head=None
        self.cnt=cnt

    def get(self, index: int) -> int:
        if index < 0 or index >= self.cnt:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node=ListNode(val)
        new_node.next=self.head
        self.head=new_node
        self.cnt+=1
        return None

    def addAtTail(self, val: int) -> None:
        curr=self.head
        prev=self.head
        if self.cnt == 0:
            self.addAtHead(val)
            return
        while curr:
            prev=curr
            curr=curr.next
        prev.next=ListNode(val)
        self.cnt+=1
        return None


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.cnt:
            return

        current = self.head
        new_node = ListNode(val)

        if index == 0:
            new_node.next = current
            self.head = new_node
            self.cnt+=1
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.cnt+=1


    def deleteAtIndex(self, index: int) -> None:
        curr=self.head
        i=0
        if index < 0 or index > self.cnt-1:
            return
        if index == 0:
            self.head=self.head.next
            self.cnt-=1
            return None
        for i in range(1,index):
            curr=curr.next
        if index == self.cnt:
            curr.next=None
            return None

        curr.next=curr.next.next
        self.cnt-=1
        return None

    def __str__(self):
        i=0
        curr=self.head
        a=[]
        
        # while curr and i< size:
        #     a+=[(i,curr.val)]
        #     i+=1
        #     curr=curr.next
        # return str(a)
        while curr:
            a+=[(i,curr.val)]
            i+=1
            curr=curr.next
        return str(a)




# Your MyLinkedList object will be instantiated and called as such:
# test=["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtTail","deleteAtIndex","deleteAtIndex"]
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
#         print(obj1,f"deleteAtIndex {test1[k][0]}",obj1.cnt)
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

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
    
#         fast = head
#         slow = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 return True
    
#         return False
# size=10
# pos=10
# obj1=MyLinkedList()
# for _ in range(size):
#     obj1.addAtTail(random.randint(10,100))

# print(obj1.__str__(size))

# pos=3
# curr=obj1.head
# while curr.next: 
#     curr=curr.next
# tail = curr

# curr=obj1.head
# for _ in range(pos):
#     curr=obj1.head.next

# tail.next=curr

# answer=Solution



# print(obj1.__str__(size),pos-1)
# print(answer.hasCycle(head=obj1.head,self=answer))

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.


# Do not modify the linked list.
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         slow,fast=head,head
#         has_loop=False
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 has_loop=True
#                 slow=head
#                 break
#         if has_loop:
#             while fast and slow!=fast:
#                 slow=slow.next
#                 fast=fast.next
#             return slow
#         else:
#             return None

            
# size=10
# pos=3
# obj1=MyLinkedList()
# for _ in range(size):
#     obj1.addAtTail(random.randint(10,100))

# print(obj1.__str__(size))

# curr=obj1.head
# while curr.next: 
#     curr=curr.next
# tail = curr

# curr=obj1.head
# for _ in range(pos):
#     curr=obj1.head.next

# tail.next=curr

# answer=Solution



# print(obj1.__str__(size),pos-1)
# print(answer.detectCycle(head=obj1.head,self=answer).val)

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

obj1=MyLinkedList()
obj2=MyLinkedList()
m=10
n=10
skip=1
for _ in range(m):
    obj1.addAtTail(random.randint(10,100))
for _ in range(n):
    obj2.addAtTail(random.randint(10,100))


curr=obj1.head if m<n else obj2.head
curr2=obj2.head if m<n else obj1.head

while curr.next:
    curr=curr.next

for _ in range(skip):
    curr2=curr2.next
    if _ == skip-1:
        curr.next=curr2


print(obj1,"obj1")
print(obj2,"obj2")

headA=obj1.head
headB=obj2.head

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # a, b = headA, headB
        # while a != b:
        #     a = headB if not a else a.next
        #     b = headA if not b else b.next
        # return a
        # Find the lengths of both lists
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        
        # Reset the pointers to the original heads
        currA, currB = headA, headB
        
        # Move the longer list's pointer ahead by the difference in lengths
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
        
        # Traverse both lists until they intersect
        while currA != currB:
            currA = currA.next
            currB = currB.next
        
        return currA  # Return the intersected node (or None if no intersection)
    
print(Solution.getIntersectionNode(headA=headA,headB=headB,self=Solution).val)


# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        p1,p2=dummy,dummy
        for _ in range(n):
            p2=p2.next
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
        return dummy.next


obj1=MyLinkedList()

size=1
n=1
for _ in range(size):
    obj1.addAtHead(random.randint(10,1000))

print(obj1)

ans=Solution.removeNthFromEnd(self=Solution,head=obj1.head,n=n)
i=0
curr=ans
a=[]
while curr:
    a+=[(i,curr.val)]
    i+=1
    curr=curr.next
print(str(a))


# Given the head of a singly linked list, reverse the list, and return the reversed list.

obj1=MyLinkedList()
size=10
for _ in range(size):
    obj1.addAtHead(random.randint(10,1000))
print(obj1)

def reverse_linked_list_iterative(head):
    prev, current = None, head
    

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        i=0
        curr=prev
        a=[]
        while curr:
            a+=[(i,curr.val)]
            i+=1
            curr=curr.next
        print(a)

    return prev

# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5

reversed_head = reverse_linked_list_iterative(obj1.head)

def reverse_linked_list_retry(head):
    current=head
    while current:
        new_node=current
        
    pass

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
















