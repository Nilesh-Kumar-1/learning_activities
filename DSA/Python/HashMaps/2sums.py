class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums=dict()
        for i in range(len(nums)):
            if (target-nums[i]) in dict_nums:
                return [i,dict_nums[target-nums[i]]]
            dict_nums.update({nums[i]:i})