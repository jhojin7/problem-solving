"""
"""
from __solver import *
class Solution:
    def divide(self,dividend:int, divisor:int) -> int:
        print(dividend, divisor)
        # sign for return val
        sign = 1
        if dividend*divisor < 0:
            sign = -1
        n = divisor
        cnt = 0
        while abs(n) <= abs(dividend):
            cnt += 1
            n += divisor
            print(n,sign*cnt)
        return sign*cnt

# print(Solution().divide(10,3))
# print(Solution().divide(10,-3))
# print(Solution().divide(1,1))
# print(Solution().divide(7,-3))
# print(Solution().divide(-2147483648,-1))


print(-123<<1)
print(-123>>2)
print(10>>1)