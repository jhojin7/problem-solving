"""
https://leetcode.com/submissions/detail/711725538/
"""
from __solver import *
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run = 0
        for i in range(len(nums)):
            run += nums[i]
            nums[i] = run
        return nums

nums = [1,2,3,4]
# nums = [1,1,1,1,1]
# nums = [3,1,2,10,1]
print(Solution().runningSum(nums))