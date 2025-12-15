# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = self.get_frequency_map(s)
        map_t = self.get_frequency_map(t)
        return True if map_s == map_t else False
    
    def get_frequency_map(self, s: str) -> dict:
        map_frequency = {}
        for char in s:
            map_frequency[char] = map_frequency.get(char, 0) + 1
        return map_frequency