# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        maxf = 0
        res_map = dict()
        res = -float('inf')

        for r in range(n):
            res_map[s[r]] = res_map.get(s[r],0) + 1
            maxf = max(maxf,res_map[s[r]]) # replacing the character which is least frequent

            while (r - l + 1) - maxf > k or res_map[s[l]] == 0:
                res_map[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res