from typing import List


# o=import typing
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            l = i + 1
            r = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                continue
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # print([i,l,r, sum])
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    temp = [[nums[l],nums[i],nums[r]]]
                    result = result + temp 
                    l += 1
                    r -= 1
                    # we can mainly break the while loop as same nums[i] can have multiple combination which we can have the target.
                    while nums[l] == nums[l - 1] and l < r: # added to remove the dulplicates
                        l += 1
        return list(result)
    
print(Solution.threeSum(Solution,[-1,0,1,2,-1,-4]))

a = (1,)

a = a + a
# print(a.sort())