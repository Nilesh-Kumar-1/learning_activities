# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
class ListNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.set = [ListNode(-1,-1) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return 
            curr = curr.next
        curr.next=ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.set[index].next

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.set[index]

        while curr.next and curr:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next
        return
    
    def hash(self, key):
        return key % len(self.set)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)