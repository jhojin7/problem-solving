"""
https://leetcode.com/submissions/detail/717347181/
"""
from __solver import *
class Solution:
    def climbStairs(self, n: int) -> int:
        """dp memoization. think fibonacci."""
        ways = [0 for _ in range(n)]
        for i in range(n):
            if i < 2:
                ways[i] = i+1
            else:
                ways[i] += ways[i-1] + ways[i-2]
        print(ways)
        return ways[-1]

print("ret",Solution().climbStairs(4))
print("ret",Solution().climbStairs(3))