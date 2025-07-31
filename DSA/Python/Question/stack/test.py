class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # def find_middle(self):
    #     # TODO
    #     if self.length%2 == 0:
    #         mid=self.length//2
    #         index = [mid,mid-1]
    #     else:
    #         mid=self.length//2
    #         index = [mid]
    #     result = list()
    #     for i in index:
    #         result.append(self.get_by_index(i))
    #     return result
    # def get_by_index(self,index):
    #     current = self.head
    #     for _ in range(index):
    #         current = current.next
    #     return current.next
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def __str__(self):
        result = str()
        current = self.head
        while current:
            result += str(current.val) + "-->"
            current = current.next
        return result
    def remove_duplicates(self):
        if self.head is None:
            return
        node_vals = set()  # set to store unique node vals
        current_node = self.head
        node_vals.add(current_node.val)
        while current_node.next:
            if current_node.next.val in node_vals:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_vals.add(current_node.next.val)
                current_node = current_node.next
        self.tail = current_node


# # Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes./

# LinkedLists = LinkedList()


# for i in range(2):
#     LinkedLists.append(i)
#     LinkedLists.append(i)
# print(LinkedLists)
# # LinkedLists.remove(0)
# # print(.val)
# print(LinkedLists.find_middle().val)
# LinkedLists.remove_duplicates()
# print(LinkedLists)



# # mid = 10//2
# # mid2 = 10%2
# # print(mid,mid2)

    
l1 = LinkedList()


for i in [1,2,2,1,2]:
    l1.append(i)
    # LinkedLists.append(i)
# l1.append(2)
print(l1)

l2 = LinkedList()
for i in range(4,9):
    l2.append(i)

print(l2)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def append(self, val):
    #     new_node = Node(val)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1
    # def __str__(self):
    #     result = str()
    #     current = self.head
    #     while current:
    #         result += str(current.val) + "-->"
    #         current = current.next
    #     return result
class Solution(object):
    def reversed(self,head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def isPalindrome(self, head):
        # reversed_head = self.reversed(head)
        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
        #     while curr_l1 and curr_l1.val <= curr_l2.val:
        #         l3.next = Node(curr_l1.val)
        #         # l3.next.next = Node(curr_l2.val)
        #         curr_l1 = curr_l1.next
        #         # curr_l2 = curr_l2.next
        #         l3 = l3.next
        #     if curr_l2 and curr_l1 is None:
        #         l3.next = curr_l2
        #         return head.next
        #     while curr_l2 and curr_l2.val <= curr_l1.val:
        #         l3.next = Node(curr_l2.val)
        #         # l3.next.next = Node(curr_l1.val)
        #         # curr_l1 = curr_l1.next
        #         curr_l2 = curr_l2.next
        #         l3 = l3.next
        #     if curr_l2 and curr_l1 is None:
        #         l3.next = curr_l2
        #         return head.next
        #     curr_l1 = curr_l1.next
        #     curr_l2 = curr_l2.next
        #     l3 = l3.next
        # if curr_l1:
        #     l3.next = curr_l1
        # elif curr_l2:
        #     l3.next = l2
        # return head.next
    
sol = Solution()
test = Solution.isPalindrome(sol,l1.head)
print(test)
while test is not None:
    print(test.val)
    test = test.next
# print(test.val)
