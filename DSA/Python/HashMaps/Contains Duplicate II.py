class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        Map = {}
        for i in range(len(nums)):
            if nums[i] in Map and abs(i - Map[nums[i]]) <= k:
                    return True
            Map[nums[i]] = i
        return False