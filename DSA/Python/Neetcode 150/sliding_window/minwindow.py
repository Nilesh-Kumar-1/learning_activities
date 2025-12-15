# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        result = ""
        min_len = float('inf')
        window = dict()
        dict_t = dict()
        if nt > ns:
            return result
        
        for i in t:
            dict_t[i] = dict_t.get(i,0) + 1
        
        for l in range(ns): # initialize l
            if s[l] in dict_t:
                break
        
        for r in range(l, ns):
            if s[r] in dict_t:
                window[s[r]] = window.get(s[r], 0) + 1

                while l < r and window[s[r]] > dict_t[s[r]] or s[l] not in dict_t:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1

                if window == dict_t:
                    if min_len >= r - l + 1:
                        result = s[l:r+1]
                        min_len = r - l + 1
        print(result)
        return result

def test_minWindow():
    sol = Solution()

    # Test Case 1: Basic example from prompt
    assert sol.minWindow("OUZODYXAZV", "XYZ") == "YXAZ", "Test Case 1 Failed"

    # Test Case 2: Exact match
    assert sol.minWindow("xyz", "xyz") == "xyz", "Test Case 2 Failed"

    # Test Case 3: No possible window
    assert sol.minWindow("x", "xy") == "", "Test Case 3 Failed"

    # Test Case 4: t has duplicate characters
    assert sol.minWindow("aaabcab", "aabc") == "aabc", "Test Case 4 Failed"

    # Test Case 5: Multiple valid windows, return shortest
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC", "Test Case 5 Failed"

    # Test Case 6: Case sensitivity
    assert sol.minWindow("aAbBcC", "abc") == "", "Test Case 6 Failed"  # lowercase mismatch

    # Test Case 7: Case-sensitive match
    assert sol.minWindow("aAbBcC", "AbC") == "bBcC", "Test Case 7 Failed"

    # Test Case 8: t longer than s
    assert sol.minWindow("abc", "abcd") == "", "Test Case 8 Failed"

    # Test Case 9: t is a single character
    assert sol.minWindow("abcde", "c") == "c", "Test Case 9 Failed"

    # Test Case 10: s and t are both single characters and match
    assert sol.minWindow("a", "a") == "a", "Test Case 10 Failed"

    # Test Case 11: Large input with match near the end
    long_s = "x" * 500 + "abc" + "y" * 500
    assert sol.minWindow(long_s, "abc") == "abc", "Test Case 11 Failed"

    print("✅ All test cases passed!")

# Run the test
test_minWindow()