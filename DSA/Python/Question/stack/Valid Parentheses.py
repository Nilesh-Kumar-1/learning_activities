# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

a = [9,8,0]
print(a[-1])

def isValid(self, s: str) -> bool:
        val = {')':'(','}':'{',']':'['}
        val_list = [0]
        for i in s:
            if i not in val:
                val_list.append(i)
            elif i in val:
                if val_list[-1] == val[i]:
                    val_list.pop()
                else:
                    val_list.append(i)
        if len(val_list) == 1:
            return True
        return False