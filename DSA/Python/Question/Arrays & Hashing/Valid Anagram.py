# Valid Anagram
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

        def get_freq(string):
            map_string = {}
            for i in string:
                if i in map_string:
                    map_string[i] += 1
                else:
                    map_string[i] = 1
            return map_string

        map_s = get_freq(s)
        map_t = get_freq(t)


        return map_s == map_t
    
# A diffrent solution

s = "racecar"
t = "carrace"

def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        print(count)

        for val in count:
            if val != 0:
                return False
        return True

isAnagram(s,t)