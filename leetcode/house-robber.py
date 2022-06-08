"""
https://leetcode.com/submissions/detail/717390458/
"""
from __solver import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        """dp"""
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) # max of two
        for i in range(2,len(dp)):
            # max sum between prev house max 
            # vs. prev-prev house + this house
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        print(dp)
        return dp[-1]

tc = testcases("""
[1,2,3,1]
[2,7,9,3,1]
[2,1,1,2] #3
[0]
""")
while tc: print("ret",Solution().rob(*tc.popleft()))