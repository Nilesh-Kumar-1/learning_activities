# 3Sum
# Solved 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5


# Recommended Time & Space Complexity
# You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
nums = [-2,0,1,1,2]
def threeSum(nums: list[int]) -> list[list[int]]:
        lngth = len(nums)
        res = []
        for i in range(lngth):
            for j in range(lngth):
                if i != j:
                    for k in range(lngth):
                        if i != k and j != k:
                            if nums[i] + nums[j] + nums[k] == 0:
                                triplet = sorted([nums[i], nums[j], nums[k]])
                                if triplet not in res:
                                    res.append(triplet)
                                triplet = []
        return res

def threeSuma(nums: list[int]) -> list[list[int]]:
        lngth = len(nums)
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                 break # As nums is a sorted arrary all the elements after nums will always be greater than 0 so we can never achive target of 0.
            if i > 0 and num == nums[i - 1]: # to remove chance of duplicates as num[i] should be unique
                continue 
            l = i + 1
            r = lngth - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1# we can mainly break the while loop as same nums[i] can have multiple combination which we can have the target.
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # added to remove the dulplicates
                        l += 1
                    # break
        return res

print(threeSuma(nums))

for i,j in enumerate(nums):
     print(i,j)