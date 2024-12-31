class ListNode():
    def __init__(self, key):
        self.val = key
        self.next = None

class MyHashSet(ListNode):

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index=self.hash(key)
        curr=self.set[index]

        while curr.next:  # to skip dummy nodes
            if curr.next.val==key:
                return
            curr=curr.next
        curr.next=ListNode(key)
        return

    def remove(self, key: int) -> None:
        index=self.hash(key)
        curr=self.set[index]

        while curr.next:  # to skip dummy nodes
            if curr.next.val==key:
                curr.next=curr.next.next
                return
            curr=curr.next
        return

    def contains(self, key: int) -> bool:
        index=self.hash(key)
        curr=self.set[index]

        while curr.next:  # to skip dummy nodes
            if curr.next.val==key:
                return True
            curr=curr.next
        return False
    def hash(self,val):
        return val % len(self.set)


# Your MyHashSet object will be instantiated and called as such:
test=["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
test1=[[], [1], [2], [1], [3], [2], [2], [2], [2]]
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

for i in test:
    print(i,test1[k],k,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if i == "MyLinkedList":
        obj1=MyLinkedList()
    if i == "add":
        obj1.add(test1[k][0])
        print(obj1,f"add {test1[k][0]}")
    if i == "remove":
        print(obj1,f"deleteAtIndex {test1[k][0]}",obj1.cnt)
        obj1.deleteAtIndex(test1[k][0])
        print(obj1)
    if i == "contains":
        print(obj1.get(test1[k][0]))
    k+=1
print(obj1)