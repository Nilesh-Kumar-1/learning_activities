class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        lsum, rsum, tsum = 0, 0 ,0
        for l in range(0,k):
          lsum += cardScore[l]
        tsum = max(tsum, lsum + rsum)

        for r in range(-1, -k-1, -1):
          lsum -= cardScore[l]
          l -= 1
          rsum += cardScore[r]

          tsum = max(tsum, lsum + rsum)
        return tsum

sol = Solution()
print(sol.maxScore(cardScore=[1], k=1))