"""
https://leetcode.com/submissions/detail/711134067/
"""
from __solver import *
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # insertion sort
        for i in range(1,len(nums)):
            for j in range(i,0,-1):
                # check
                n1 = str(nums[j-1])+str(nums[j])
                n2 = str(nums[j])+str(nums[j-1])
                # if swapping needed, swap
                if n1 < n2:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        # str(int("00")) => "0"
        return str(int("".join(map(str,nums))))

nums = [10,2]
# nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))