"""
https://leetcode.com/submissions/detail/708691585/
"""
from __solver import *
class Solution:
    def missingNumber(self, nums: List[int])->int:
        nums.sort()
        print(nums)
        # if first value isnt 0, return 0
        if nums[0]!=0: return 0
        # if last value isnt n, return n
        if nums[-1]!= len(nums): return len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]+1 != nums[i]:
                return nums[i-1]+1

nums = [3,0,1]
nums = [1,2,3,4,5,6,7]
nums = [0,1,2,3,4,5,6,7]
print(Solution().missingNumber(nums))
nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]