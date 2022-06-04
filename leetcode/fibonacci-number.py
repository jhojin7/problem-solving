"""
https://leetcode.com/submissions/detail/714332340/
"""
import collections
class Solution:
    dp = collections.defaultdict(list)
    def fib(self, n: int) -> int:
        if n<2: return n
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        if self.dp[n]:
            return self.dp[n]
print(Solution().fib(3))