class Solution:
    def firstUniqChar(self, s: str) -> int:
        Map = {}
        for i in s:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1
        for i in range (len(s)):
            if Map[s[i]] == 1:
                return i
        return -1
    
# Better Solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Use a fixed-size array to store the first occurrence index of each character
        index = [-1] * 26
        # Array to mark characters seen more than once
        seen_multiple = [False] * 26
        
        # Populate the arrays
        for i, char in enumerate(s):
            pos = ord(char) - ord('a')
            if index[pos] == -1:
                index[pos] = i
            else:
                seen_multiple[pos] = True
        
        # Find the smallest index of a unique character
        min_index = float('inf')
        for i in range(26):
            if index[i] != -1 and not seen_multiple[i]:
                min_index = min(min_index, index[i])
        
        return min_index if min_index != float('inf') else -1
