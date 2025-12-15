# Products of Array Except Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        is_zeros = {0:0}
        prod = 1

        for num in nums:
            if num != 0:
                prod = prod*num
            else:
                is_zeros[0] += 1
        res = []
        if is_zeros[0] > 1: return [0] * len(nums)
        for num in nums:
            if is_zeros[0] == 1:
                res = res + [prod] if num == 0 else res + [0]   
            else:
                res.append(prod//num)
        return res
        