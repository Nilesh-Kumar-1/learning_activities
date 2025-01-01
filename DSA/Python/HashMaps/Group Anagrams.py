def groupAnagrams(strs: list[str]) -> list[list[str]]:
        Map = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in Map:
                Map[sorted_str].append(i)
            else:
                Map[sorted_str] = [i]
        return list(Map.values())


from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        count = [0 for _ in range(26)]
        for char in word:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(word)

    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

