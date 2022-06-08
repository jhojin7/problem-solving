"""
https://leetcode.com/submissions/detail/717316443/
"""
from __solver import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """memoization"""
        dp = [nums[0]]
        for i in range(1,len(nums)):
            x = max(nums[i], nums[i]+dp[i-1])
            dp.append(x)
        return max(dp)

    def maxSubArray(self, nums):
        """kadane's Algorithm"""
        current, largest = 0, 0
        for n in nums:
            current = max(n, n+current)
            largest = max(current, largest)
        return largest

    # def divideNconquer(self, nums: List[int]) -> int:
    #     """divide and conquer"""
    #     # stop recursion
    #     if len(nums) == 1:
    #         return nums[0]
    #     # divide
    #     left = self.maxSubArray(nums[:len(nums)//2])
    #     right = self.maxSubArray(nums[len(nums)//2:])
    #     # conquer
    #     print(nums, left, right)
    #     # return largest of:
    #     return max(left+right, left, right)


tc = testcases("""
[-2,1,-3,4,-1,2,1,-5,4]
[1]
[5,4,-1,7,8]
""")
while tc: print("ret ",Solution().maxSubArray(*tc.popleft()))