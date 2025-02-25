# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        slow, fast = dummy, dummy
        
        for _ in range(n+1):
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next


#  In this code we
# 1. Create a dummy node to simplify the code
# 2. Initialize two pointers, slow and fast, both pointing to the dummy node
# 3. Move the fast pointer n+1 steps ahead so that the difference between slow and fast pointers are always n + 1
# 4. Move both pointers one step at a time until the fast pointer reaches the end of Linked List
# 5. At this point, the slow pointer will be at the node right before the nth
# 6. Remove the nth node by changing the next pointer of the slow node to the next of next of slow node
# 7. Return the head of the modified Linked List by returning the next of dummy node
# Time complexity: O(L), where L is the number of nodes in the Linked List
# Space complexity: O(1), as we are only using a constant amount of space to store the dummy node and the two pointers.
