# Definition for singly-linked list.
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        def findLength(Head):
            length = 0
            curr = Head
            while curr.next:
                length += 1
                curr = curr.next
            return length
        
        diff = findLength(headA) - findLength(headB)
        
        
        if diff > 0:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(-diff):
                headB = headB.next
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
    
# What we did
# 1) We first checked the length of both linked list
# 2) Then we moved the pointer (lenA - lenB) times so that the pointers on both the list are at same distance from the intersecting node
# 3) Then we moved both the pointers one by one and if they meet then it is the intersecting node 
        