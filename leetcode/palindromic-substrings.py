"""
https://leetcode.com/submissions/detail/704594875/
"""
from __solver import *
class Solution:
    def countSubstrings(self, s: str) -> int:
        # if s is single char, return 1
        if len(s) == 1: return 1
        # check for s==s[::-1]
        ans = 0
        # print(s==s[::-1],s,s[::-1])
        if s == s[::-1]: ans += 1
        # main
        for l in range(1,len(s)):
            for i in range(len(s)-l+1):
                s1 = s[i:i+l]
                # print(s1 == s1[::-1],s1,s1[::-1])
                if s1 == s1[::-1]:
                    ans += 1
        # print(ans)
        return ans

# "abc"
# "aaa"
# "abcdeb"
# "abcdcb"
# "hlsakfkagsuebkvabufavieaiucdjiznejcdkuuhfaiuck"
Solution.countSubstrings(Solution,"abcdcba")