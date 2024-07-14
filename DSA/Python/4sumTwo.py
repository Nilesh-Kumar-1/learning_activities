class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        sum_count = {}
    
        # Calculate frequencies of sums of pairs from nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum_count[num1 + num2] = sum_count.get(num1 + num2, 0) + 1
                
        # Count pairs from nums3 and nums4 whose sum is opposite of previously calculated sums
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in sum_count:
                    count += sum_count[target]
                    
        return count
        
test=Solution()
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [0, 0]
nums4 = [0, 0]
print(test.fourSumCount(nums1, nums2, nums3, nums4))  # Output: 2