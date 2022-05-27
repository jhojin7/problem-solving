"""
https://leetcode.com/submissions/detail/708105253/
"""
from __solver import *
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num != 0:
            cnt += 1
            print(cnt, num)
            # if even, divide by 2
            if num%2 == 0:
                num //= 2
            # if odd, subtract 1
            else: 
                num -= 1
        # if num is 0, return cnt
        return cnt
print(Solution().numberOfSteps(14))