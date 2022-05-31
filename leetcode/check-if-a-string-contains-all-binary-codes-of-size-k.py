"""
https://www.adamsmith.haus/python/answers/how-to-convert-an-integer-to-binary-and-keep-the-leading-zeros-in-python
https://leetcode.com/submissions/detail/710978828/
"""
from __solver import *
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        _set = set()
        for i in range(len(s)-k+1):
            _set.add(s[i:i+k])
        print(sorted(_set), len(_set))
        return (2**k==len(_set))
        # s_bin = int(s,2)
        # for _ in range(len(s)):
        #     for j in range(2**k):
        #         s1 = bin(s_bin)[2:]
        #         s2 = format(j,f"0{k}b")
        #         print(s1,s2)
        #         if s2 not in s:
        #             return False
        #     s_bin = s_bin>> 1
        # return True

        # print(s,k)
        # # binaries of len(k)
        # binaries = []
        # for x in range(2**k):
        #     binaries.append(
        #         # format(1,"02b")=>01
        #         format(x,f"0{k}b"))
        # for b in binaries:
        #     # fill binary str
        #     print(b,s)
        #     if b not in s:
        #         return False
        # return True

# print(bin(int(s,2)>>10)[2:], bin(1)[2:])
# s,k = "00111111111010100110000010001",3
# s,k = "0110",1
# s,k = "0110",2
s,k = "00110",2
ret = Solution().hasAllCodes(s,k)
print(ret)