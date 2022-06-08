"""
https://leetcode.com/submissions/detail/716999058/
diff between substring and subsequence: https://leetcode.com/problems/remove-palindromic-subsequences/discuss/2124524/Do-not-mix-up-"substring"-with-"subsequence"!!!
"""
from __solver import *

class Solution:
    # return 1 if s == s[::-1] else 2
    def removePalindromeSub(self, s: str) -> int:
        # worst case: if s is not palindrome:
        # remove all aaaa...a sub"sequence" in 1st step,
        # then remove bbb...b sub"sequence" in 2nd step.

        # if already palindrome, return 1
        if s == s[::-1]: return 1
        # find left, right from middle
        if len(s) % 2 == 1:
            # if len is odd
            left = len(s)//2-1
            right = len(s)//2+1
        else:
            # if len is even
            left = len(s)//2-1
            right = len(s)//2
        
        # move pointers outward from middle
        while left >= 0 and right < len(s):
            # if left!=right: return 2 
            if s[left] != s[right]:
                return 2
            left -= 1
            right += 1

# only a and b
tc = testcases("""
"ababa"
"abb"
"baabb"
"bbaabaaa"#2
""")
while tc:
    print(Solution().removePalindromeSub(*tc.pop()))