def topKFrequent(nums: list[int], k: int) -> list[int]:
        Map = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            Map[i] = Map.get(i , 0) + 1
        for num, frequency in Map.items():
            freq[frequency].append(num)
            
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
nums = [1,1,1,2,2,3]
k = 2                
print(topKFrequent(nums,k))

# for j in [[],1,[4]]:
#      print(j)