import random
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            index = self.Map[val]
            last_val = self.numList[-1]
            self.numList[index] = last_val
            self.numList.pop()
            self.numMap[last_val] = index
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your MyHashSet object will be instantiated and called as such:
test=["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
test1=[[], [1], [2], [1], [3], [2], [2], [2], [2]]
k = 0
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

for i in test:
    print(i,test1[k],k,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if i == "RandomizedSet":
        obj1=RandomizedSet()
    if i == "insert":
        obj1.insert(test1[k][0])
        print(obj1,f"add {test1[k][0]}")
    if i == "remove":
        print(obj1,f"remove {test1[k][0]}")
        obj1.remove(test1[k][0])
        print(obj1)
    if i == "getRandom":
        print(obj1.getRandom())
    k+=1
print(obj1)