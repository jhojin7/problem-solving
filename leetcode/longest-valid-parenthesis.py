"""
https://leetcode.com/submissions/detail/706087136/
https://leetcode.com/problems/longest-valid-parentheses/discuss/2068590/C++-or-Short-and-simple-solution
"""
from __solver import *
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        print(s)
        # https://leetcode.com/problems/longest-valid-parentheses/discuss/2068590/C++-or-Short-and-simple-solution
        stack = [-1]
        maxval = 0
        for i in range(len(s)):
            print(maxval,stack)
            if s[i]=="(": 
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxval = max(maxval,i-stack[-1])
        return maxval

""
s = "(()"
print(Solution().longestValidParentheses(s))
s = ")()())"
s = "()(()"
s = "())()"
# ret = Solution().longestValidParentheses("()()()((((())))()()()()())))(((((()()((()()()()(()(()))()(")