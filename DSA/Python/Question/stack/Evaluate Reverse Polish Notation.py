# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

a = [1,4,6]
print(a.pop(),a.pop())

def evalRPN(tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                r1 = stack.pop()
                r2 = stack.pop()
                res = r1 + r2
            elif tokens[i] == "-":
                r1 = stack.pop()
                r2 = stack.pop()
                res = r2 - r1
                # stack.append(stack[i-2] - stack[i-1])
            elif tokens[i] == "*":
                r1 = stack.pop()
                r2 = stack.pop()
                res = r2 * r1
                # stack.append(stack[i-2] * stack[i-1])
            elif tokens[i] == "/":
                r1 = stack.pop()
                r2 = stack.pop()
                res = int(r2/r1)
                # stack.append(stack[i-2] // stack[i-1])
            else:
                res = int(tokens[i])
                # stack.append(int(tokens[i]))
            stack.append(res)
            print(stack, tokens[i])
        return stack.pop()

tokens=["2","1","+","3","*"]
print(evalRPN(tokens)) # Output: 22