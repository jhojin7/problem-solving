"""
https://leetcode.com/submissions/detail/712683929/
https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
https://ko.wikipedia.org/wiki/2%EC%9D%98_%EB%B3%B4%EC%88%98
"""
from __solver import *
# def half_adder(a:int, b:int)-> Tuple[int,int]:
#     sum = a^b
#     carry = a&b
#     return sum,carry
# # print(half_adder(2,4))

class Solution:
    @staticmethod
    def full_adder(a:int, b:int, carry_in)-> Tuple[int,int]:
        sum = a^b^carry_in
        carry_out = (a&b)|(carry_in&(a^b)) 
        return sum,carry_out

    def getSum(self, a: int, b: int) -> int:
        # pre processing to 2's complement
        MASK = 0xFFFFFFFF #2**32
        _a = format(a&MASK,"032b")
        _b = format(b&MASK,"032b")
        ans,cin,cout = [],0,0
        for i in range(31,-1,-1):
            bitA,bitB = int(_a[i]),int(_b[i])
            cin = cout
            s,cout = self.full_adder(bitA,bitB,cin)
            ans.append(s)
        # if negative
        if cout==1: 
            ans.append(cout)
        # print(cout,len(ans),ans)

        res = int(''.join(map(str,ans[::-1])),2)&MASK
        # if result is beyond int(1000)
        if res>1000:
            # mask and negate to get -int
            res = ~(res^MASK)
        return res

# print(math.floor(math.sqrt(1000)))
# _b = "10000000000000000000000000000001"
# print(len(_b))
nums=(1000,1000)
nums=(-1000,-1000)
# print(format(-1000,"0b"))
print(Solution().getSum(*nums))

# comp2 = int(3^0xFF)+1
# print(~(comp2^0xFF))# -3
# # print(int(format(,"04b")))

def getSum(a,b):
    INTMAX = 0x7FFFFFFF
    MASK = 0xFFFFFFFF
    a,b = (a^b)&MASK,((a&b)<<1)&MASK