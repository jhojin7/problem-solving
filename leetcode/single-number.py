"""
https://leetcode.com/submissions/detail/712635952/
https://leetcode.com/problems/single-number/discuss/1771791/Python3-ONE-LINER-**-Explained
"""
from __solver import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            # print(ans,num,ans^num)
            ans ^= num
        return ans
nums = [2,2,1]
nums = [4,1,2,1,2]
# nums = [1]
print(Solution().singleNumber(nums))
print(operator.xor(2,1),2^2^1^1^4)
print(functools.reduce(operator.xor, nums))