"""
https://leetcode.com/submissions/detail/711455784/
"""
from __solver import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        print(idx)
        if idx<len(nums) and nums[idx] == target:
            return idx
        else: 
            return -1

nums,target = [-1,0,3,5,9,12],9#4
nums, target = [-1,0,3,5,9,12],2#-1
print(Solution().search(nums,target))