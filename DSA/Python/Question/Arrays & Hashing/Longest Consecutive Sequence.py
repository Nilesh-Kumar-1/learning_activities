# Longest Consecutive Sequence
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

nums = [2,20,4,10,3,4,5]

def longestConsecutive(nums: list[int]) -> int:
        hash_nums = set(nums)
        print(hash_nums)
        res = 0
        streak = 0

        for i in nums:
            # if res >= len(nums)//2:
            #     return res
            if i-1 not in hash_nums:
                j = i
                while j in hash_nums:
                    streak += 1
                    print(j)
                    j += 1
                res = max(streak, res)
                streak = 0
        return res

print(longestConsecutive(nums))


        