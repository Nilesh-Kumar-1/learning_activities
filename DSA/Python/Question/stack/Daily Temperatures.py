# Daily Temperatures
# Solved 
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]
# Example 2:

# Input: temperatures = [22,21,20]

# Output: [0,0,0]
# Constraints:

# 1 <= temperatures.length <= 1000.
# 1 <= temperatures[i] <= 100


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

# Brute force 
def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        res = list()
        for i in range(length):
            mini = 0
            flag = False
            for j in range(i+1, length):
                if temperatures[i] < temperatures[j]:
                    flag = True
                    break
            if flag:
                mini = j-i
            res.append(mini)
        return res

inputs = [30,38,30,36,35,40,28]
def dailyTempoptimised(temperatures):
        length = len(temperatures)
        res = [0 for _ in range(length)]
        stack = []
        for i,j in enumerate(temperatures):
            while stack != [] and j > stack[-1][1]:
                    index, nums = stack.pop()
                    res[index] = i-index
            stack.append((i,j))
        return res

print(dailyTempoptimised(inputs))

