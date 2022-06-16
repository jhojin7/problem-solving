"""
tle:https://leetcode.com/submissions/detail/723361822/
ac: https://leetcode.com/submissions/detail/723415753/
"""
from __solver import *
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        ans = ""
        dp = [[False]*len(s) for _ in range(len(s))]
        # all single letter substr are palindromes
        for i in range(len(s)):
            dp[i][i] = True
            # update ans
            ans = s[i]
        # all two ch substr are pali if s[i]==s[j] 
        for i in range(len(s)-1):
            dp[i][i+1] = s[i]==s[i+1]
        
        # loop throuh rest of dp
        # for i in range(len(s)-1,-1,-1):
        #     for j in range(i+1,len(s)):
        for j in range(1,len(dp)):
            for i in range(j):
                # if ends are not equal, not palindrome
                if s[i] != s[j]:
                    continue
                # if other substr is palindrome
                if j-i==1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    # update ans
                    if len(ans) < j+1-i:
                        ans = s[i:j+1]
        return ans


    def notlongestPalindrome(self, s: str) -> str:
        print(s)
        # if s itself is palindrome, return itself
        if s == s[::-1]: return s
        palind = {} 
        maxlen = 0
        # for i in range(len(s)-1):
        #     for j in range(1,len(s)):
        #         substr = s[i:j]
        for j in range(1,len(s)+1):
            for i in range(j):
                substr = s[i:j]
        
                # if substr is palindrome
                if substr == substr[::-1]:
                    # save key:len, val:substr
                    # overwrite old
                    palind[len(substr)] = substr 
                    # update maxlen
                    maxlen = max(maxlen,len(substr))
        # print(palind, maxlen)
        # retrun substr at maxlen
        return palind[maxlen]
tc = testcases("""
"babad"
"cbbd"
"abb"
"ab"
"aacbcaffbcffcb"
""")
while tc: print(Solution().longestPalindrome(*tc.pop()))