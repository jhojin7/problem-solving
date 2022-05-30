"""
https://leetcode.com/problems/divide-two-integers/discuss/2089533/Easy-Solution-in-C++
https://leetcode.com/submissions/detail/710709363/
"""
from numpy import infty
from __solver import *
class Solution:
    # def divide(self,dividend:int, divisor:int) -> int:
    #     print(dividend, divisor)
    #     # sign for return val
    #     sign = 1
    #     if dividend*divisor < 0:
    #         sign = -1
    #     n = divisor
    #     cnt = 0
    #     while abs(n) <= abs(dividend):
    #         cnt += 1
    #         n += divisor
    #         print(n,sign*cnt)
    #     return sign*cnt
    def divide(self,dividend:int, divisor:int) -> int:
        # https://leetcode.com/problems/divide-two-integers/discuss/2089533/Easy-Solution-in-C++
        #############
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        divid, divis = abs(dividend), abs(divisor)
        ans = 0
        # divid>=n,divid=divis*ans
        # while n is under divid 
        while divid >= divis:
            mul, tmp = divis, 1
            while mul <= divid-mul:
                mul += mul
                tmp += tmp
            # increnent ans
            ans += tmp
            divid -= mul
        # check for +- with xor
        if (dividend < 0) ^ (divisor < 0):
            return -ans
        return ans
        

# print(Solution().divide(10,3))
# print(Solution().divide(10,3))
print(Solution().divide(1,1))
print(Solution().divide(0,1))
# print(Solution().divide(7,-3))
print(Solution().divide(-2147483648,-1)) #2147483647