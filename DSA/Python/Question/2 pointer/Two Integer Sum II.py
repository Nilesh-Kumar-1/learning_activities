# Two Integer Sum II
# Solved 
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # for i in range(len(numbers)):
        #     l, r = i + 1, len(numbers) - 1
        #     tmp = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r - l)//2
        #         if numbers[mid] == tmp:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < tmp:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return []
        return self.compare(numbers, target)

    def compare(self,num,tar):
        i = 0
        j = len(num) - 1

        while i < j:
            first = num[i]
            last = num[j]
            sums = first + last

            if sums > tar:
                j -= 1
            elif sums < tar:
                i += 1
            elif sums == tar:
                return [i+1 , j+1]
        return False



        