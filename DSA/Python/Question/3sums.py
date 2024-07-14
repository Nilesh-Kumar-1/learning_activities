class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        target=0
        res,trip = [], []
        def ksum(k, start,target):
            if k !=2 :
                for i in range(start, len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    trip.append(nums[i])
                    ksum(k - 1, i + 1, target - nums[i])
                    trip.pop()
                return
            end = len(nums)-1
            l,r = start, end
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(trip + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        ksum(3, 0,0)
        return res
    
test=Solution()
nums=[-1,0,1,2,-1,-4]
target=0
print(test.threeSum(nums))

