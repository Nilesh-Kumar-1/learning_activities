# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_frequency(nums):
            hash_freq = {}
            for i in nums:
                hash_freq[i] = hash_freq.get(i,0) + 1
            return hash_freq
        freq_list = [[] for _ in range(len(nums)+1)]

        get_frequency_hash = get_frequency(nums)
        # print(get_frequency_hash)
        for num in get_frequency_hash:
            frequency = get_frequency_hash[num]
            freq_list[frequency].append(num)
        
        res = []
        for i in range(-1,-len(freq_list),-1):
            if len(res) == k:
                return res
            if freq_list[i] != [] and len(res)<k:
                res += freq_list[i]
        return res[:k]

sol = Solution()
# Example usage
nums = []
k = 1
print(sol.topKFrequent(nums, k))  # Output: [1, 2]

        