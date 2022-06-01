"""
https://leetcode.com/submissions/detail/711797500/
https://leetcode.com/submissions/detail/711805432/
"""
from __solver import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     i1, i2 = 0, len(numbers)-1
    #     while i1 != i2:
    #         if numbers[i1] + numbers[i2] < target:
    #             i1+=1
    #         elif numbers[i1] + numbers[i2] > target:
    #             i2-=1
    #         else:
    #             return [i1+1,i2+1]

        for k,v in enumerate(numbers):
            expected = target-v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i<len(nums) and numbers[i+k+1] == expected:
                return [k+1,i+k+2]

        
numbers, target = [-999,2,7,11,15],9
# numbers, target = [-999,2,3,4],6
# numbers, target = [-999,-1,0],-1
print(Solution().twoSum(numbers, target))