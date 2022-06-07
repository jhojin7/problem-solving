"""
https://leetcode.com/submissions/detail/716554864/
"""
from __solver import *

# from ast import literal_eval
class Solution:
    def compute(self,left:list[int], right:list[int], ch:str)->list[int]:
        if not left or not right:
            return left
        ret = []
        for l in left:
            for r in right:
                # print(f"compute {l}{ch}{r}")
                ret.append(eval(
                    str(l)+ch+str(r)))
        return ret

    def diffWaysToCompute(self, expression: str) -> List[int]:
        answers = []
        # print(expression)
        if expression.isdigit():
            return [int(expression)]
        for i,ch in enumerate(expression):
            if not ch.isdigit():
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # print("recursion",left,right)
                calc = self.compute(left,right,ch)
                # if calc and calc.isdigit():
                answers.extend(calc)
            # # if ch is digit
            # else:
        # print(answers)
        return answers

tc = testcases("""
"2-1-1"
"2*3-4*5"
"1-1*1+1-1"
""")
while tc:
    print(Solution().diffWaysToCompute(*tc.popleft()))