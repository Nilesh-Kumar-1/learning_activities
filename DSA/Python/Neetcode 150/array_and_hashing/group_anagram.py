# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_frequency(strings: str) -> tuple:
            # should used OrderedDict to maintain the order of characters
            map_strings = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
            for char in strings:
                map_strings[char] = map_strings.get(char,0) + 1
            return tuple(map_strings.values())
        map_strs = {}
        for s in strs:
            map_s = check_frequency(s)
            if map_s in map_strs:
                map_strs[map_s].append(s)
            else:
                map_strs[map_s] = [s]
            # print(map_strs)
        return list(map_strs.values())