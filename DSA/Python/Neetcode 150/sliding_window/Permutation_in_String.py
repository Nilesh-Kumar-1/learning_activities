# Permutation in String
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false
# Constraints:

# 1 <= s1.length, s2.length <= 1000

class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     def get_frequency(strings:str) -> dict:
    #         map_string = dict()
    #         for s in strings:
    #             map_string[s] = map_string.get(s,0) + 1
    #         return map_string
    #     n1, n2 = len(s1), len(s2)
    #     count = 0
    #     l, r = 0, 0
    #     map_s1 = get_frequency(s1)
        
    #     while l < n2:
    #         # print(s2[l],s2[l] in map_s1)
    #         if s2[l] in map_s1:
    #             r = l
    #             # count = 0
    #             while r < n2:
    #                 if map_s1.get(s2[r],0) > 0:
    #                     map_s1[s2[r]] -= 1
    #                     count += 1
    #                 else:
    #                     break
    #                 if count == n1:
    #                     return True
    #                 r += 1
    #         elif n2 - l < n1: 
    #             return False
    #         if l >= r:
    #             l += 1
    #         else:
    #             while l < r and r < n2 and map_s1.get(s2[r],0) == 0:
    #                 map_s1[s2[l]] += 1
    #                 l += 1
    #                 count -= 1
    #     return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        
        map_s1, map_s2 = dict(), dict()
        
        for i in range(n1):
            map_s1[s1[i]] = map_s1.get(s1[i],0) + 1
            map_s2[s2[i]] = map_s2.get(s2[i],0) + 1
        
        l = 0
        for r in range(n1,n2):
            if map_s1 == map_s2:
                return True
            map_s2[s2[l]] = map_s2.get(s2[l],0) - 1
            map_s2[s2[r]] = map_s2.get(s2[r],0) + 1

            if map_s2[s2[l]] == 0:
                del map_s2[s2[l]]
            l += 1

        return map_s1 == map_s2



        

        
        

def test_checkInclusion():
    sol = Solution()  # Create an instance of the class

    # Test Case 1: Basic permutation exists
    assert sol.checkInclusion("abc", "lecabee") == True, "Test Case 1 Failed"

    # Test Case 2: No permutation present
    assert sol.checkInclusion("abc", "lecaabee") == False, "Test Case 2 Failed"

    # Test Case 3: Exact match
    assert sol.checkInclusion("abc", "abc") == True, "Test Case 3 Failed"

    # Test Case 4: Permutation at the end
    assert sol.checkInclusion("abc", "zzzzcab") == True, "Test Case 4 Failed"

    # Test Case 5: Permutation at the beginning
    assert sol.checkInclusion("abc", "bcahello") == True, "Test Case 5 Failed"

    # Test Case 6: Repeated characters in s1
    assert sol.checkInclusion("aabc", "caaab") == False, "Test Case 6 Failed"

    # Test Case 7: s2 shorter than s1
    assert sol.checkInclusion("abcd", "abc") == False, "Test Case 7 Failed"

    # Test Case 8: s1 and s2 are both single characters
    assert sol.checkInclusion("a", "a") == True, "Test Case 8 Failed"
    assert sol.checkInclusion("a", "b") == False, "Test Case 9 Failed"

    # Test Case 9: s1 is longer than s2
    assert sol.checkInclusion("abcde", "abc") == False, "Test Case 10 Failed"

    # Test Case 10: Large input with permutation in the middle
    long_s2 = "x" * 500 + "bac" + "y" * 500
    assert sol.checkInclusion("abc", long_s2) == True, "Test Case 11 Failed"

    assert sol.checkInclusion("acd", "dcda") == True, "Test Case 12 Failed"

    print("All test cases passed!")

# Run the test
test_checkInclusion()