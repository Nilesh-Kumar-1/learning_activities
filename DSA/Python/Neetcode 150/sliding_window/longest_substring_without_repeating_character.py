# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        res_map = dict()
        res = -float('inf')

        for r in range(n):
            res_map[s[r]] = res_map.get(s[r],0) + 1
            while s[l] in res_map and res_map[s[r]] > 1:
                res_map[s[l]] = res_map.get(s[l],0) - 1
                if res_map[s[l]] == 0:
                    del res_map[s[l]]
                l += 1
            res = max(len(res_map), res)
        print(res)
        return res if res != -float('inf') else 0

def test_lengthOfLongestSubstring():
    sol = Solution()

    # Test Case 1: Example from prompt
    assert sol.lengthOfLongestSubstring("zxyzxyz") == 3, "Test Case 1 Failed"

    # Test Case 2: All same characters
    assert sol.lengthOfLongestSubstring("xxxx") == 1, "Test Case 2 Failed"

    # Test Case 3: All unique characters
    assert sol.lengthOfLongestSubstring("abcdef") == 6, "Test Case 3 Failed"

    # Test Case 4: Empty string
    assert sol.lengthOfLongestSubstring("") == 0, "Test Case 4 Failed"

    # Test Case 5: Single character
    assert sol.lengthOfLongestSubstring("a") == 1, "Test Case 5 Failed"

    # Test Case 6: Repeating pattern
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "Test Case 6 Failed"

    # Test Case 7: Long unique prefix
    assert sol.lengthOfLongestSubstring("abcdefghijaabc") == 10, "Test Case 7 Failed"

    # Test Case 8: Special characters
    assert sol.lengthOfLongestSubstring("!@#$%^&*()") == 10, "Test Case 8 Failed"

    # Test Case 9: Mixed case sensitivity
    assert sol.lengthOfLongestSubstring("aAbBcC") == 6, "Test Case 9 Failed"
    # Test Case 9: Mixed case sensitivity
    assert sol.lengthOfLongestSubstring("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert") == 17, "Test Case 9 Failed"

    # Test Case 10: Long string with duplicates
    long_str = "abcde" * 200  # length = 1000
    assert sol.lengthOfLongestSubstring(long_str) == 5, "Test Case 10 Failed"

    print("All test cases for test_lengthOfLongestSubstring passed!")

# Run the test
test_lengthOfLongestSubstring()
