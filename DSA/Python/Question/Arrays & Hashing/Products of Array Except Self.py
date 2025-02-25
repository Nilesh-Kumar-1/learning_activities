# Products of Array Except Self
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

test= [1,2,4]

res= map(1,test)

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         mul = 1
#         mul2 = 1
#         res = []
#         contains_zero = False
#         for i in range(len(nums)):
#             if i!= 0:
#                 mul = mul * nums[i-1]
#             for j in range(i+1, len(nums)):
#                 mul2 = mul2 * nums[j]
#             res.append(mul * mul2)
#             mul2 = 1
            
#         return res

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res        