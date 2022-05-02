"""
https://leetcode.com/submissions/detail/691622965/
"""
from __solver import *
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x%2 == 0]\
            +[x for x in nums if x%2 == 1]
        for i in range(0,len(nums)):
            if nums[i]%2 == 0:
                even_nums.append(nums.pop(i))
        return even_nums + nums