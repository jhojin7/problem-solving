"""
# time limit exceeded
https://leetcode.com/submissions/detail/694446349/
"""
from __solver import *

import collections
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        for _ in range(len(s)):
            for i in range(len(s)):
                substr = s[i:i+k]
                # if only single type of char, remove i:i+k
                if len(substr) == k and len(collections.Counter(substr)) == 1:
                    s = s[:i] + s[i+k:]
        return ''.join(s)

        stack = list(s[0:1]) # k min is 2
        for i in range(0,len(s)):
            stack.append(s[i])
            print(stack[-k:],len(collections.Counter(stack[-k:])))
            if len(collections.Counter(stack[-k:]))==1:
                for _ in range(k): stack.pop()
                print(stack)
        print(''.join(stack))
        return ''.join(stack)






inputs = [
"abcd"
,2
,"deeedbbcccbdaa"
,3
,"pbbcggttciiippooaais"
,2
]
while inputs:
    Solver.solve(Solution, inputs.pop(0), inputs.pop(0))