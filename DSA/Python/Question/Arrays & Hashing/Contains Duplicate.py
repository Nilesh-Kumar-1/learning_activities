# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        my_set = set(nums)
        if len(my_set) == len(nums):
            return False
        else:
            return True

a = [1,5,3,3]

print(len(set(a)))