"""
https://leetcode.com/submissions/detail/721715576/
"""
from __solver import *
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                # max between i-1, j-1, i-1/j-1/isEqual
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], 
                    dp[i-1][j-1] + (word1[i-1] == word2[j-1]))
                    # note that dp[i-1][j-1]+...
        # dp[-1][-1] = longest common subsequence
        # num of del steps = count of chars not common
        return len(word1)+len(word2)-2*dp[-1][-1]

tc = testcases("""
"sea"
"eat"
"leetcode"
"etco"
""",2)
while tc:
    print(Solution().minDistance(*tc.popleft()))