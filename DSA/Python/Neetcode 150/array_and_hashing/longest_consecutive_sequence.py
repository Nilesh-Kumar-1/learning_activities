# Longest Consecutive Sequence
# Solved 
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        i = 0
        lens = 0
        maxi = float('-inf')
        for num in set_nums:
            if num - 1 not in set_nums:
                i = num
                lens = 0
                while i in set_nums:
                    lens += 1
                    i += 1
                maxi = max(maxi, lens)
        return maxi if maxi != float('-inf') else 0
sol = Solution()
# Example usage
print(sol.longestConsecutive([2,20,4,10,3,4,5]))  # Output: 4
print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))  # Output: 7
print(sol.longestConsecutive([]))  # Output: 0
