# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

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

hash_map = {1:1,2:3,(1,3):2}
tuple_of_zeros = (0,) * 26
print((0,) * 26)

# print(hash_map.get(90,6))

print([1] + [2])

print(ord("b")-ord("a"))

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        hash_result = {}
        def get_freq(string):
            char = [0 for _ in range(26)]
            for i in range(len(string)):
                char[ord(string[i]) - ord("a")] += 1
                # hash_string[i] = 1 + hash_string.get(i,0)
            return char

        for i in strs:
            list_freq = get_freq(i)
            print(hash_map)
            if tuple(list_freq) in hash_result:
                hash_result[tuple(list_freq)] += [i]
            else:
                 hash_result[tuple(list_freq)] = [i]
        return list(hash_result.values())
strs = ["act","pots","tops","cat","stop","hat"]

print(groupAnagrams(strs))