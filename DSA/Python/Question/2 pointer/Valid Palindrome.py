# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: 
s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.

import string

check = set(string.ascii_lowercase + string.digits)
# print(string.ascii_lowercase + string.digits)

def cleanup(s):
    return ''.join(c.lower() for c in s if c.lower() in string.ascii_lowercase + string.digits)

print(cleanup(s) == cleanup(s)[::-1])

def pointer(s):
    i = 0
    j = len(s) - 1
    while i < j:
        start = s[i].lower()
        end = s[j].lower()
        if start in check and end in check:
            if start != end:
                return False
            i += 1
            j -= 1
        elif start not in check:
            i += 1
        elif end not in check:
            j -= 1
    return True

print(pointer(s))
