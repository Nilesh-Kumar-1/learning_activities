# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

a= [1,3,6]
print(a.pop())
print(a)

class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # mini = -float(inf)
        if self.mini != []:
            if self.mini[-1] >= val:
                self.mini.append(val)
        else:
            self.mini.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.mini[-1] == val:
                self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        


Inputs = ["MinStack", "push", -2, "push", -2, "push", -3, "push", -3, "getMin", "pop", "getMin"]

length = len(Inputs)
res = []
i = 0
while i < length:
    
    if Inputs[i] == "MinStack":
        minStack = MinStack()
        res.append(None)
    print(minStack)
    if Inputs[i] == "push":
        minStack.push(Inputs[i+1])
        i += 1
        res.append(None)
    if Inputs[i] == "getMin":
        res.append(minStack.getMin())
        print(minStack.getMin())
    if Inputs[i] == "pop":
        minStack.pop()
        res.append(None)
    i += 1
print(res)
print(minStack)