# Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

height = [1,7,2,5,4,7,3,6]
def maxArea(heights: list[int]) -> int:
        lngth = len(heights)
        maxi = 0
        for i in range(lngth):
            for j in range(lngth):
                maxi = max(min(heights[i],heights[j])*abs(i-j),maxi)
        return maxi

print(maxArea(height))

# 2nd approach
# We can use the two pointer algorithm. One pointer is at the start and the other at the end. 
# At each step, we calculate the amount of water using the formula (j - i) * min(heights[i], heights[j]). 
# Then, we move the pointer that has the smaller height value. 
# In the formula, the amount of water depends only on the minimum height. 
# Therefore, it is appropriate to replace the smaller height value.


def maxArea(heights: list[int]) -> int:
        maxi = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            maxi = max(min(heights[i],heights[j])*abs(i-j),maxi)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] <= heights[j]:
                i += 1
        return maxi