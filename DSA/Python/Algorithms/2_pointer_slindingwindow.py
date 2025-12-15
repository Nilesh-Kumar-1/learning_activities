# Maximum Points You Can Obtain from Cards


# 0

# 100
# Medium

# Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. 
# The score is the sum of the scores of the chosen cards.



# Return the maximum score that can be obtained.


# Examples:
# Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3

# Output : 15

# Explanation : Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4 , 5 , 6.

# Th score is 4 + 5 + 6 => 15.

# Input : cardScore = [5, 4, 1, 8, 7, 1, 3 ] , k = 3

# Output : 12

# Explanation : In first step we will choose card from beginning with score of 5.

# In second step we will choose the card from beginning again with score of 4.

# In third step we will choose the card from end with score of 3.

# The total score is 5 + 4 + 3 => 12

# Input : cardScore = [9, 10, 1, 2, 3, 5] , k = 5

# 30
# 29
class Solution:
    def maxScore(self, cardScore, k):
      lsum = 0
      rsum = 0
      max_sum = lsum + rsum


      for l in range(k):
        lsum += cardScore[l]
      max_sum = max(max_sum,lsum + rsum)

      r = -1
      for l in range(k-1,-1,-1):
        lsum -= cardScore[l]
        rsum += cardScore[r]

        r -= 1

        max_sum = max(max_sum,lsum + rsum)
      return max_sum

######################################################################
# Longest Substring Without Repeating Characters


# 0

# 100
# Medium

# Given a string, S. Find the length of the longest substring without repeating characters.


# Examples:
# Input : S = "abcddabac"

# Output : 4

# Explanation : The answer is "abcd" , with a length of 4.

# Input : S = "aaabbbccc"

# Output : 2

# Explanation : The answers are "ab" , "bc". Both have maximum length 2.

# Input : S = "aaaa"

class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        n= len(s)
        r,l = 0, 0
        res = ""
        if n == 0:
            return 0
        char_index = {}
        max_length = 0
        for i in range(n):
            if s[i] not in char_index:
                char_index[s[i]] = i
                r = i
            elif s[i] in char_index and char_index[s[i]] >= l:
                max_length = max(max_length, r-l+1)
                l = char_index[s[i]] + 1
                char_index[s[i]] = i
                
        return max(max_length, r-l+1)
    
           
# Solution 2
class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        n= len(s)
        r,l = 0, 0
        if n == 0:
            return 0
        char_index = {}
        max_length = 0
        for i in range(n):
            if s[i] not in s[l:r+1]:
                r = i
            elif s[i] in s[l:r+1]:
                max_length = max(max_length, r-l+1)
                while s[l] != s[i]:
                    l += 1
                l += 1
                
        return max(max_length, r-l+1)
# Example usage

# Max Consecutive Ones III


# 0

# 100
# Hard

# Given a binary array nums and an integer k, flip at most k 0's.

# Return the maximum number of consecutive 1's after performing the flipping operation.


# Examples:
# Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3

# Output : 10

# Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).

# The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].

# The number of consecutive 1's is 10.

# Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3

# Output : 9

# Explanation : The underlines 1's are obtained by flipping 0's in the new array.

# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].

# The number of consecutive 1's is 9.

class SolutionLongestOnes:
    def longestOnes(self, nums, k):
        # Brute force solution would be O(n^2) which is not optimal
        zero_count = 0
        max_length = 0
        for l in range(len(nums)):
            zero_count = zero_count + 1 if nums[l] == 0 else zero_count
            for r in range(l+1, len(nums)):
                zero_count = zero_count + 1 if nums[r] == 0 else zero_count
                if zero_count <= k:
                    max_length = max(max_length, r - l + 1)
                else:
                    max_length = max(max_length, 1)
                    break
                # zero_count = 0
        # print(f"Max length of subarray with at most {k} zeros: {max_length}")
        return max_length
        # # We can use sliding window technique to solve this problem in O(n) time complexity
        # #your code goes here
        n = len(nums)
        l = 0
        r = 0
        max_length = 0
        zero_count = 0
        # print(f"{'r':>2} {'nums[r]':>8} {'zero_count':>12} {'l':>2} {'Window':>20} {'max_length':>12}")
        # print("-" * 60)

        for r in range(n):
            if nums[r] == 1 or zero_count < k:
                max_length = max(max_length, r-l+1)
                if nums[r] == 0:
                    zero_count += 1
            else:
                # print("l:", l, "r:", r, "zero_count:", zero_count, "max_length:", max_length, "nums[l:r+1]:", nums[l:r+1])
                zero_count += 1
                while nums[l] != 0:
                    l += 1
                l += 1
                zero_count -= 1
            window = nums[l:r+1]
        #     print(f"{r:>2} {nums[r]:>8} {zero_count:>12} {l:>2} {str(window):>20} {max_length:>12}")
        # print("-" * 60)
        # print(f"Final max_length: {max_length}")
        return max_length
# Example usage

print(True or False)

def test_longestOnes():
    sol = SolutionLongestOnes()

    # ✅ Test Case 1: Example from prompt
    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 3) == 10

    # ✅ Test Case 2: Another example from prompt
    assert sol.longestOnes([0,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1,1], 3) == 9

    # ✅ Test Case 3: No flips allowed
    assert sol.longestOnes([1,0,1,0,1,0,1], 0) == 1

    # # # ✅ Test Case 4: All 1s
    assert sol.longestOnes([1,1,1,1,1], 2) == 5

    # # # ✅ Test Case 5: All 0s, flip all
    assert sol.longestOnes([0,0,0,0], 4) == 4

    # # # ✅ Test Case 6: Flip fewer than total 0s
    assert sol.longestOnes([0,0,0,0], 2) == 2

    # # # ✅ Test Case 7: Alternating pattern
    assert sol.longestOnes([1,0,1,0,1,0,1,0], 2) == 5  # Flip two 0s to get 1,1,1,1,1

    # # # ✅ Test Case 8: Empty array
    assert sol.longestOnes([], 3) == 0

    # # # ✅ Test Case 9: k larger than number of 0s
    assert sol.longestOnes([1,0,1,1,0,1], 10) == 6

    # # # ✅ Test Case 10: Long run of 1s interrupted by a few 0s
    assert sol.longestOnes([1]*50 + [0]*3 + [1]*50, 3) == 103

    print("All test cases for test_longestOnes passed!")

test_longestOnes()

# Fruit Into Baskets


# 0

# 100
# Hard

# There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.



# The goal is to gather as much fruit as possible, adhering to the owner's stringent rules:



# 1) There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.

# 2) Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.

# 3) Once reaching a tree with fruit that cannot fit into any basket, stop.



# Return the maximum number of fruits that can be picked.


# Examples:
# Input : fruits = [1, 2, 1]

# Output : 3

# Explanation : We will start from first tree.

# The first tree produces the fruit of kind '1' and we will put that in the first basket.

# The second tree produces the fruit of kind '2' and we will put that in the second basket.

# The third tree produces the fruit of kind '1' and we have first basket that is already holding fruit of kind '1'. So we will put it in first basket.

# Hence we were able to collect total of 3 fruits.

# Input : fruits = [1, 2, 3, 2, 2]

# Output : 4

# Explanation : we will start from second tree.

# The first basket contains fruits from second , fourth and fifth.

# The second basket will contain fruit from third tree.

# Hence we collected total of 4 fruits.

# Input : fruits = [1, 2, 3, 4, 5]

# 1
# 2
# 3
# 4

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

class SolutiontotalFruits:
    def totalFruits(self, fruits):
        # brute force solution would be O(n^2) which is not optimal
        # we can use two pointers to find the maximum length of the subarray with at most
        # max_length = 0
        # for l in range(len(fruits)):
        #     for r in range(l, len(fruits)):
        #         if len(set(fruits[l:r+1])) <= 2:
        #             max_length = max(max_length, r - l + 1)
        #             print(max_length)
        #         else:
        #             break
        # print(f"Max length of subarray with at most 2 types of fruits: {max_length}")
        # return max_length
        # we can use sliding window technique to solve this problem in O(n) time complexity
        # fruits = [1, 2, 1, 2, 3, 4, 5]

        l = 0
        fruits_count = {}
        max_length = 0
        for r in range(len(fruits)):
            if fruits[r] in fruits_count:
                fruits_count[fruits[r]] += 1
            else:
                fruits_count[fruits[r]] = 1
            
            while len(fruits_count) > 2:
                fruits_count[fruits[l]] -= 1
                if fruits_count[fruits[l]] == 0:
                    del fruits_count[fruits[l]]
                l += 1
            
            max_length = max(max_length, r - l + 1)
        return max_length

def test_totalFruits():
    sol = SolutiontotalFruits()

    # ✅ Basic examples
    assert sol.totalFruits([1, 2, 1]) == 3
    assert sol.totalFruits([1, 2, 3, 2, 2]) == 4
    assert sol.totalFruits([1, 2, 3, 4, 5]) == 2

    # ✅ All same fruit
    assert sol.totalFruits([1, 1, 1, 1]) == 4

    # ✅ Only two types, alternating
    assert sol.totalFruits([1, 2, 1, 2, 1, 2]) == 6

    # ✅ Three types, with longest in middle
    assert sol.totalFruits([1, 2, 3, 2, 2, 3, 3, 1]) == 6  # [2,3,2,2,3,3]

    # ✅ Edge case: empty array
    assert sol.totalFruits([]) == 0

    # ✅ Edge case: one fruit
    assert sol.totalFruits([7]) == 1

    # ✅ Stress test: long array with only two types
    assert sol.totalFruits([1, 2] * 50000) == 100000

    print("All fruits test cases passed!")

test_totalFruits() 

# Longest Substring With At Most K Distinct Characters


# 0

# 100
# Hard

# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.


# Examples:
# Input : s = "aababbcaacc" , k = 2

# Output : 6

# Explanation : The longest substring with at most two distinct characters is "aababb".

# The length of the string 6.

# Input : s = "abcddefg" , k = 3

# Output : 4

# Explanation : The longest substring with at most three distinct characters is "bcdd".

# The length of the string 4.

# Input : s = "abccab" , k = 4

# 3
# 4
# 6
# 5

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= s.length <= 105
# 1 <= k <= 26

class SolutionkDistinctChar:
    def kDistinctChar(self, s, k):
        # Brute force solution would be O(n^2) which is not optimal
        # max_length = 0
        # for l in range(len(s)):
        #     for r in range(l, len(s)):
        #         if len(set(s[l:r+1])) <= k:
        #             max_length = max(max_length, r - l + 1)
        #         else:
        #             break
        # return max_length
        #your code goes here
        # We can use sliding window technique to solve this problem in O(n) time complexity
        max_length = 0
        l = 0
        char_count = {}
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            while len(char_count) > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

def test_kDistinctChar():
    sol = SolutionkDistinctChar()

    # ✅ Basic examples
    assert sol.kDistinctChar("aababbcaacc", 2) == 6  # "aababb"
    assert sol.kDistinctChar("abcddefg", 3) == 4     # "bcdd"
    assert sol.kDistinctChar("abccab", 4) == 6       # entire string

    # ✅ All same character
    assert sol.kDistinctChar("aaaaaaa", 1) == 7

    # ✅ All unique characters, k = 1
    assert sol.kDistinctChar("abcdef", 1) == 1

    # ✅ All unique characters, k = len(s)
    assert sol.kDistinctChar("abcdef", 6) == 6

    # ✅ Repeating pattern
    assert sol.kDistinctChar("abcabcabc", 2) == 2     # max 2 distinct

    # ✅ Edge case: empty string
    assert sol.kDistinctChar("", 3) == 0

    # ✅ Edge case: k = 0
    assert sol.kDistinctChar("abc", 0) == 0

    # ✅ Edge case: k = 26, full alphabet
    assert sol.kDistinctChar("abcdefghijklmnopqrstuvwxyz", 26) == 26

    # ✅ Stress test: long string with limited distinct characters
    long_str = "aabbccddeeffgg" * 1000  # 14,000 characters
    assert sol.kDistinctChar(long_str, 3) >= 3  # Should not crash

    print("All test cases for test_kDistinctChar passed!")

test_kDistinctChar()

# Number of Substrings Containing All Three Characters


# 0

# 100
# Hard

# Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.


# Examples:
# Input : s = "abcba"

# Output : 5

# Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "abc" , "abcb" , "abcba" , "bcba" , "cba".

# Input : s = "ccabcc"

# Output : 8

# Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "ccab" , "ccabc" , "ccabcc" , "cab" , "cabc" , "cabcc" , "abc" , "abcc".

# Input : s = "abccba"

# 4
# 9
# 7
# 5

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= s.length <= 5*104
# s consist only of characters 'a

class SolutionSubstringsWithAllChars:
    def substringsWithAllChars(self, s):
        # Brute force solution would be O(n^3) which is not optimal
        # max_length = 0
        # for l in range(len(s)):
        #     for r in range(l, len(s)):
        #         if len(set(s[l:r+1])) == 3:
        #             max_length += 1
        # # print(f"Max length of substrings with all three characters: {max_length}")
        # return max_length
    
        # We can use sliding window technique to solve this problem in O(n) time complexity
        max_length = 0
        l = 0
        char_count = {}
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            
            while len(char_count) == 3:
                max_length += len(s) - r
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
        return max_length

def test_substringsWithAllChars():
    sol = SolutionSubstringsWithAllChars()

    # ✅ Basic examples
    assert sol.substringsWithAllChars("abcba") == 5
    assert sol.substringsWithAllChars("ccabcc") == 8
    assert sol.substringsWithAllChars("abccba") == 7

    # ✅ All same character
    assert sol.substringsWithAllChars("aaaaa") == 0

    # ✅ Only two characters
    assert sol.substringsWithAllChars("ababab") == 0
    assert sol.substringsWithAllChars("cccccc") == 0

    # ✅ All three characters, minimal case
    assert sol.substringsWithAllChars("abc") == 1

    # ✅ Repeating pattern
    assert sol.substringsWithAllChars("abcabcabc") == 28  # All substrings of length ≥ 3 that contain a,b,c

    # ✅ Edge case: empty string
    assert sol.substringsWithAllChars("") == 0

    # ✅ Edge case: string of length 1 or 2
    assert sol.substringsWithAllChars("a") == 0
    assert sol.substringsWithAllChars("ab") == 0

    # ✅ Stress test: long string with only two characters
    long_str = "a" * 10000 + "b" * 10000
    assert sol.substringsWithAllChars(long_str) == 0

    # ✅ Stress test: long string with all three characters
    long_str = "abc" * 1000  # 3000 characters
    assert sol.substringsWithAllChars(long_str[:10]) >= 1  # Should not crash

    print("All test cases for test_substringsWithAllChars passed!")

test_substringsWithAllChars()

# Longest Repeating Character Replacement


# 0

# 100
# Hard

# Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.


# Examples:
# Input : s = "BAABAABBBAAA" , k = 2

# Output : 6

# Explanation : we can change the B present at index 0 , 3 (0 base indexing) to A.

# The new string is "AAAAAABBBAAA".

# The substring "AAAAAA" is the longest substring having same letter with length 6.

# Input : s = "AABABBA" , k = 1

# Output : 4

# Explanation : The underlined characters are changed in the new string obtained.

# The new string is "AABBBBA". The substring "BBBB" is the answer.

# There are other ways to achieve this answer.

# Input : s = "ABCDEF" k = 1

# 1
# 2
# 3
# 4

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= s.length <= 105
# 0 <= k <= s.length
# s contains only English uppercase letters.

# Similar Problems

class SolutioncharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        #your code goes here
        # max_length = 0
        # n = len(s)
        # for l in range(n):
        #     diff = 0
        #     for r in range(l,n):
        #         diff = diff + 1 if s[r] != s[l] else diff
        #         if diff > k:
        #             break
        #         max_length = max(max_length, r-l+1)
        # return max_length
    
        # We can use sliding window technique to solve this problem in O(n) time complexity
        max_length = 0
        l = 0
        char_count = {}
        for r in range(len(s)):
            # create a hash map to count the characters in the current window
            char_count[s[r]] = char_count.get(s[r], 0) + 1

            # Remove characters from the left until the condition is satisfied
            while (r-l + 1) - char_count[s[l]] > k or char_count[s[l]] == 0:
                char_count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length



def test_characterReplacement():
    sol = SolutioncharacterReplacement()

    # ✅ Basic examples
    assert sol.characterReplacement("BAABAABBBAAA", 2) == 6
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("ABCDEF", 1) == 2

    # ✅ All same character
    assert sol.characterReplacement("AAAAAA", 2) == 6

    # ✅ All unique characters, k = 0
    assert sol.characterReplacement("ABCDEFG", 0) == 1

    # ✅ All unique characters, k = 3
    assert sol.characterReplacement("ABCDEFG", 3) == 4  # Replace 3 to match one

    # ✅ Repeating pattern
    assert sol.characterReplacement("ABABABAB", 2) == 5  # Replace 2 Bs to A or vice versa

    # ✅ Edge case: empty string
    assert sol.characterReplacement("", 2) == 0

    # ✅ Edge case: string of length 1
    assert sol.characterReplacement("A", 0) == 1

    # ✅ Edge case: k = len(s)
    assert sol.characterReplacement("ABCDEFG", 7) == 7  # Can make all same

    # ✅ Stress test: long string with alternating characters
    long_str = "AB" * 5000  # 10,000 characters
    # assert sol.characterReplacement(long_str, 5000) >= 5000  # Should not crash

    print("All test cases for test_characterReplacement passed!")

test_characterReplacement()

# Binary Subarrays With Sum
# 0

# 100
# Hard

# Given a binary array nums and an integer goal. Return the number of non-empty subarrays with a sum goal.



# A subarray is a continuous part of the array.


# Examples:
# Input : nums = [1, 1, 0, 1, 0, 0, 1] , goal = 3

# Output : 4

# Explanation : The subarray with sum 3 are

# [1, 1, 0, 1]

# [1, 1, 0, 1, 0]

# [1, 1, 0, 1, 0, 0]

# [1, 0, 1, 0, 0, 1].

# Input : nums = [0, 0, 0, 0, 1] , goal = 0

# Output : 10

# Explanation : Some of the subarray with sum 0 are

# [0]

# [0, 0]

# [0, 0, 0]

# [0, 0, 0, 0]

# Constraints:
# 1 <= nums.length <= 3*104
# 0 <= goal <= nums.length
# nums consist of only 0 and 1.
# print("Binary Subarrays With Sum")



class SolutionnumSubarraysWithSum:
    def numSubarraysWithSum(self, nums, goal):
        #your code goes here
        # max_length = 0
        # n = len(nums)
        # sum = 0
        # for l in range(n):
        #     sum = nums[l]
        #     max_length = max_length + 1 if sum == goal else max_length
        #     for r in range(l+1, n):
        #         sum += nums[r]
        #         if sum > goal:
        #             break
        #         elif sum == goal:
        #             max_length += 1
        # print(f"Max length of subarray with sum {goal}: {max_length}")
        # return max_length
        # We can use sliding window technique to solve this problem in O(n) time complexity

        # count = 0
        # l = 0
        # sum = 0
        # n = len(nums)
        # for r in range(n):
        #     sum += nums[r]
        #     while sum > goal and l < r:
        #         sum -= nums[l]
        #         l += 1
        #     if sum == goal:
        #         temp = l
        #         while temp < r and nums[temp] == 0:
        #             count += 1
        #             temp += 1
        #         count += 1
        # print(f"Total subarrays with sum {goal}: {count}")
        # return count

        # We can use sliding window technique to solve this problem in O(n) time complexity
        # To find the number of subarrays with sum equal to goal, we can find the
        # number of subarrays with sum at most goal and subtract the number of subarrays(sum <= goal)
        # with sum at most goal - 1 from it i.e (sum <= goal) - sum<= goal - 1.

        def atMost(nums,goal):
            count = 0
            l = 0
            sum = 0
            n = len(nums)
            for r in range(n):
                sum += nums[r]
                while sum > goal and l <= r:
                    sum -= nums[l]
                    l += 1
                count += (r - l + 1)
            return count
        return atMost(nums,goal) - atMost(nums,goal-1)
            


def test_numSubarraysWithSum():
    sol = SolutionnumSubarraysWithSum()

    # ✅ Basic examples
    assert sol.numSubarraysWithSum([1, 1, 0, 1, 0, 0, 1], 3) == 4
    assert sol.numSubarraysWithSum([0, 0, 0, 0, 1], 0) == 10

    # ✅ All 1s, goal = 2
    assert sol.numSubarraysWithSum([1, 1, 1, 1], 2) == 3  # [1,1], [1,1], [1,1]

    # ✅ All 0s, goal = 0
    assert sol.numSubarraysWithSum([0, 0, 0], 0) == 6  # All combinations

    # ✅ Mixed pattern
    assert sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4  # [1,0,1], [0,1,0,1], etc.

    # ✅ Edge case: empty array
    assert sol.numSubarraysWithSum([], 0) == 0

    # ✅ Edge case: goal = 0, single 1
    assert sol.numSubarraysWithSum([1], 0) == 0

    # ✅ Edge case: goal = 1, single 1
    assert sol.numSubarraysWithSum([1], 1) == 1

    # ✅ Edge case: goal = 0, single 0
    assert sol.numSubarraysWithSum([0], 0) == 1

    # ✅ Stress test: long array with alternating 1s and 0s
    long_nums = [1, 0] * 1000  # 2000 elements
    assert sol.numSubarraysWithSum(long_nums, 1) >= 1000  # Should not crash

    print("All test cases for test_numSubarraysWithSum passed!")

test_numSubarraysWithSum()



# Count number of Nice subarrays


# 0

# 100
# Hard

# Given an array nums and an integer k. An array is called nice if and only if it contains k odd numbers. Find the number of nice subarrays in the given array nums.



# A subarray is continuous part of the array.


# Examples:
# Input : nums = [1, 1, 2, 1, 1] , k = 3

# Output : 2

# Explanation : The subarrays with three odd numbers are

# [1, 1, 2, 1]

# [1, 2, 1, 1]

# Input : nums = [4, 8, 2] , k = 1

# Output : 0

# Explanation : The array does not contain any odd number.

# Input : nums = [41, 3, 5] , k = 2

# 1
# 2
# 3
# 4

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= nums.length <= 5*104
# 1 <= nums[i] <= 105
# 1 <= k <= nums.length

class SolutionCountNiceArray:
    def numberOfOddSubarrays(self, nums, k):
        # count = 0
        # n = len(nums)
        # if n < k:
        #     return 0
        # for l in range(n):
        #     odd_count = 0
        #     for r in range(l,n):
        #         if nums[r] % 2 == 1:
        #             odd_count += 1
        #         if odd_count == k:
        #             # print(f"Found nice subarray from index {l} to {r} and odd_count: {odd_count}")
        #             count += 1
        #         elif odd_count > k:
        #             break
        # print(f"Total nice subarrays with {k} odd numbers: {count}")
        # return count

        # We can use sliding window technique to solve this problem in O(n) time complexity

        count = 0
        odd_count = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] % 2 == 1:
                odd_count = odd_count + 1

            while odd_count > k and l < r:
                odd_count = odd_count - 1 if nums[l] % 2 == 1 else 0
                l += 1

            if odd_count == k:
                count = count + 1
                temp = l
                while temp < r and nums[temp] % 2 == 0: # count the number of even numbers before the first odd number prefix logic
                    count += 1
                    temp += 1

        # print(f"Total nice subarrays with {k} is {count}, l: {l}, r: {r}, odd_count: {odd_count}")
        return count
                
        
                    
def test_numberOfOddSubarrays():
    sol = SolutionCountNiceArray()

    # Test Case 1: Basic example from prompt
    assert sol.numberOfOddSubarrays([1, 1, 2, 1, 1], 3) == 2

    # Test Case 2: No odd numbers
    assert sol.numberOfOddSubarrays([4, 8, 2], 1) == 0

    # Test Case 3: All elements are odd
    assert sol.numberOfOddSubarrays([41, 3, 5], 2) == 2

    # Test Case 4: Mixed odds and evens
    assert sol.numberOfOddSubarrays([1, 2, 3, 4, 5], 2) == 4

    # Test Case 5: All odds, small k
    assert sol.numberOfOddSubarrays([1, 3, 5, 7], 2) == 3

    # Test Case 6: All evens
    assert sol.numberOfOddSubarrays([2, 4, 6, 8], 1) == 0

    # Test Case 7: Single element, odd
    assert sol.numberOfOddSubarrays([1], 1) == 1

    # Test Case 8: Single element, even
    assert sol.numberOfOddSubarrays([2], 1) == 0

    # Test Case 9: Interleaved odds and evens
    assert sol.numberOfOddSubarrays([1, 2, 1, 2, 1], 3) == 1

    # Test Case 10: Large input, performance check
    large_input = [1]*1000 + [2]*1000
    assert sol.numberOfOddSubarrays(large_input, 1000) == 1001

    print("All test cases for test_numberOfOddSubarrays passed!")

# Run the test
test_numberOfOddSubarrays()

#  Problem: Count Subarrays with Exactly K Distinct Integers
# 📜 Statement:
# You are given an integer array nums and an integer k. A subarray is defined as a contiguous sequence of elements within nums.
# Your task is to count the number of subarrays that contain exactly k distinct integers.

# 🧠 Example:
# Input:
# nums = [1, 2, 1, 2, 3]
# k = 2


# Output:
# 7


# Explanation: The 7 subarrays with exactly 2 distinct integers are:
# - [1, 2]
# - [2, 1]
# - [1, 2]
# - [2, 1, 2]
# - [1, 2, 3]
# - [2, 1, 2, 3]
# - [1, 2, 3]

# ✅ Constraints:
# - 1 \leq \text{len(nums)} \leq 10^5
# - 1 \leq \text{nums[i]} \leq 10^5
# - 1 \leq k \leq \text{len(nums)}

# 💡 Follow-up:
# Can you solve this in O(n) time using a sliding window and frequency map?
class SolutionCountSubarraysWithKDistinct:
    def subarraysWithKDistinct(self, nums, k):
        # def atMostKDistinct(nums, k):
        #     count = 0
        #     left = 0
        #     freq_map = {}
        #     for right in range(len(nums)):
        #         freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
        #         while len(freq_map) > k:
        #             freq_map[nums[left]] -= 1
        #             if freq_map[nums[left]] == 0:
        #                 del freq_map[nums[left]]
        #             left += 1
        #         count += right - left + 1
        #     return count

        # return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
        l = 0
        n = len(nums)
        map_count = {}
        count = 0
        for r in range(n):
            map_count[nums[r]] = map_count.get(nums[r], 0) + 1
            while len(map_count) > k:
                map_count[nums[l]] -= 1
                if map_count[nums[l]] == 0:
                    del map_count[nums[l]]
                l += 1
            if len(map_count) == k:
                count += 1
                temp = l
                while temp < r and nums[temp] != nums[l]:
                    count += 1
                    temp += 1

def test_count_subarrays_with_k_distinct():
    # Test Case 1: Simple example
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7, "Test Case 1 Failed"

    # Test Case 2: Single element array
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([1], 1) == 1, "Test Case 2 Failed"

    # Test Case 3: All elements are the same
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([5, 5, 5, 5], 1) == 10, "Test Case 3 Failed"

    # Test Case 4: k greater than number of unique elements
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([1, 2, 2], 3) == 0, "Test Case 4 Failed"

    # Test Case 5: Alternating pattern
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([1, 2, 1, 2, 1], 2) == 8, "Test Case 5 Failed"

    # Test Case 6: Large array with many distinct values
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct(list(range(1, 10001)), 10000) == 1, "Test Case 6 Failed"

    # Test Case 7: Multiple valid subarrays
    assert SolutionCountSubarraysWithKDistinct.subarraysWithKDistinct([1, 2, 3, 4, 2, 1, 3], 3) == 10, "Test Case 7 Failed"

    print("✅ All test cases for test_count_subarrays_with_k_distinct passed!")


# Minimum Window Substring


# 0

# 100
# Hard

# Given two strings s and t. Find the smallest window substring of s that includes all characters in t (including duplicates) , in the window. Return the empty string "" if no such substring exists.


# Examples:
# Input : s = "ADOBECODEBANC" , t = "ABC"

# Output : "BANC"

# Explanation : The minimum window substring of string s that contains the string t is "BANC".

# Input : s = "a" , t = "a"

# Output : "a"

# Explanation : The complete string is the minimum window

# Input : s = "aAbBDdcC" , t = "Bc"

# 'BDdc'
# 'bBDdc'
# 'BDdcC'
# 'Ddc'

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 <= n , m <= 105
# n = s.length
# m = t.length
# string s and t consist of uppercase and lowercase letters.

class SolutionminWindow:
    def minWindow(self, s: str, t: str) -> str:
        # n = len(s)
        # min_window = float('inf')
        # result = ""
        # map_t = self.get_frequency(t)
        # for l in range(n):
        #     temp_map_t = map_t.copy()
        #     if s[l] in map_t:
        #         temp_map_t[s[l]] -= 1
        #         if n > 1:
        #             for r in range(l+1,n):
        #                 if s[r] in temp_map_t:
        #                     temp_map_t[s[r]] = temp_map_t[s[r]] - 1 if temp_map_t[s[r]] > 0 else temp_map_t[s[r]]
        #                 if set(temp_map_t.values()) == {0} and (r-l+1 < min_window):
        #                     min_window = min(min_window,r-l+1)
        #                     result = s[l:r+1]
        #                     # print(result + "--->" + str(min_window))
        #                     break
        #         else:
        #             if set(temp_map_t.values()) == {0} and (1 < min_window):
        #                 min_window = 1
        #                 result = s[l]
        # # print(f"Minimum window substring of s containing t is {result} with length {min_window}")
        # return result

        n = len(s)
        min_window = float('inf')
        result = ""
        map_t = self.get_frequency(t)
        # print(map_t)
        l = 0
        r = 0
        formed = 0
        required = len(map_t)
        for l in range(n):
            while r < n and formed < required and s[l] in map_t:
                if s[r] in map_t:
                    map_t[s[r]] -= 1
                    formed += 1 if map_t[s[r]] == 0 else 0
                r += 1
            if formed == required and (r - l < min_window):
                min_window = r - l 
                result = s[l:r]
                # print(result + "--->" + str(min_window))
            formed -= 1 if s[l] in map_t and map_t[s[l]] >= 0 else 0
            if s[l] in map_t:
                map_t[s[l]] += 1 
            # print(f"l: {l}, r: {r}, formed: {formed}, map_t: {map_t}")
            
            
        # print(f"Minimum window substring of s containing t is {result} with length {min_window}")
        return result

    def get_frequency(self, t: str) -> dict:
        map_t = {}
        for i in t:
            map_t[i] = map_t.get(i,0)+1
        return map_t
    
def test_minWindow(func):
    # Test Case 1: Basic example
    assert func("ADOBECODEBANC", "ABC") == "BANC", "Test Case 1 Failed"

    # Test Case 2: Single character match
    assert func("a", "a") == "a", "Test Case 2 Failed"

    # Test Case 3: No match possible
    assert func("a", "b") == "", "Test Case 3 Failed"

    # Test Case 4: Case sensitivity
    assert func("aAbBDdcC", "Bc") == "BDdc", "Test Case 4 Failed"

    # Test Case 5: Multiple valid windows, return shortest
    assert func("aaabdabcefaecbef", "abc") == "abc", "Test Case 5 Failed"

    # Test Case 6: t longer than s
    assert func("abc", "abcd") == "", "Test Case 6 Failed"

    # Test Case 7: All characters match at start
    assert func("abcde", "abc") == "abc", "Test Case 7 Failed"

    # Test Case 8: Repeated characters in t
    assert func("aaabbbc", "abc") == "abbbc", "Test Case 8 Failed"

    # Test Case 9: t has duplicates
    assert func("aaabbbc", "aabc") == "aabbbc", "Test Case 9 Failed"

    # Test Case 10: Large input performance test
    long_s = "a" * 10000 + "b" + "c"
    assert func(long_s, "abc") == "abc", "Test Case 10 Failed"

    print("All test cases for test_minWindow passed!")

test_minWindow(SolutionminWindow().minWindow)

# Example usage:
# test_minWindow(your_function_name_here)





















