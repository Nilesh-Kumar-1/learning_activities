from typing import Optional
from Design_Linked_List import MyLinkedList
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev, curr = None, head
        
    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #     return prev
    def __str__(self):
        print(12)
        curr = self.prev
        result = ''
        while curr:
            result += str(curr.val) + '-->'
            curr = curr.next
        print(result)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

obj = MyLinkedList() 
obj2 = MyLinkedList()   
for i in range(2):
    obj.addAtHead(i)
print(obj)

test = Solution()
reversed = test.reverseList(obj.node)
curr = reversed
result = ''
while curr:
            result += str(curr.val) + '-->'
            curr = curr.next
print(result)

