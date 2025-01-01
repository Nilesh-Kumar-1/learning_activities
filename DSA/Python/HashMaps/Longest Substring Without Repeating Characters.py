def lengthOfLongestSubstring(s: str) -> int:
        duplicate = set()
        maxi = -float('inf')
        count = 0
        
        for i in s:
            # print(i)
            if i in duplicate:
                maxi = max(maxi, len(duplicate))
                duplicate = set()
                duplicate.add(i)

            else:
                duplicate.add(i)
                count += 1
            maxi = max(maxi, len(duplicate))
            # print(duplicate)
        return maxi if maxi != -float('inf') else 0

def lengthOfLongestSubstring(s: str) -> int:
    duplicate = set()
    maxi = 0
    left = 0

    for right in s:
        while right in duplicate:
            duplicate.remove(s[left])
            left += 1
        duplicate.add(right)
        maxi = max(maxi, len(duplicate))
    return maxi

s = "abcabcbb"

print(lengthOfLongestSubstring(s))