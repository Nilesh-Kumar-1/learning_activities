# Top K Frequent Elements
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

nums = [1,1,2,2,2,2,3,3,3]
k = 2

# Example dictionary
example_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 2}

# Define a function that prints the item and returns its value
def print_and_return_value(item):
    print(f"Processing item: {item}")
    return item[1]

# Use the function as the key in sorted()
sorted_by_value = sorted(example_dict.items(), key=print_and_return_value)

print("Sorted by value:", sorted_by_value)

def topKFrequent(nums: list[int], k: int) -> list[int]:
        hash_nums = {}
        res = []
        for i in nums:
            hash_nums[i] = 1 + hash_nums.get(i,0)
        print(hash_nums)

        sorted_maps = sorted(hash_nums.items(), key=print_and_return_value, reverse=True)
        print(sorted_maps)

        for i in range(k):
              res.append(sorted_maps[i][0])
        print(res)
        return res
              
topKFrequent(nums,k)

# here instead of sorting based on the key value we createad list freq such that index shows the frequency of it element and its value are list of element which have frequency of index

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_nums = {}
        res = []
        freq = [[] for _ in range(len(nums)+1)]
        for i in nums:
            hash_nums[i] = 1 + hash_nums.get(i,0)
        for j in hash_nums:
             freq[hash_nums[j]].append(j)

        for k in range(len(freq),0,-1):
             for n in freq[k]:
                if len(res) == k:
                    return res
                elif freq[k] != []:
                     res.append(n)

        # sorted_maps = sorted(hash_nums.items(), key= lambda item: item[1], reverse=True)
        # print(sorted_maps)

        # for i in range(k):
        #       res.append(sorted_maps[i][0])
        print(res)
        return res

        
        
