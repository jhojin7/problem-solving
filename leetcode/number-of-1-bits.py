"""
https://leetcode.com/submissions/detail/707357173/
https://en.wikipedia.org/wiki/Hamming_weight
https://docs.python.org/3.10/library/stdtypes.html#int.bit_count
int.bit_count() since python3.10
"""
class Solution:
    def hammingWeight(self,n:int):
        # return str(n).count('1')
        # return sum([int(x) for x in list(str(n))])
        return (bin(n).count('1'))

# n = int("00000000000000000000000000001011")#3
# n = int("00000000000000000000000010000000")#1
# n = int("11111111111111111111111111111101")#31
# print(Solution().hammingWeight(n))
# 11
# 128
# 4294967293
# print(Solution().hammingWeight(11))

# n & n-1 removes one 1 from bin(n)
# repeat this until n=0 and return cnt
n = 31 # format(31,"032b")
print(n)
cnt = 0
while n:
    n &= n-1
    cnt += 1
print(cnt)