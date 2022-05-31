"""
https://leetcode.com/submissions/detail/711117432/
"""
from __solver import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i] 
        print(nums)

# nums = [2,0,2,1,1,0]
nums = [2,0,1]
Solution().sortColors(nums)