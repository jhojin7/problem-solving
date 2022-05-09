"""
from daily challenge
https://leetcode.com/submissions/detail/696001232/
"""
from __solver import * 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        numpad = {
            '2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        if digits == "": return []
        def dfs(path,idx):
            # backtrack conditions
            if len(path)==len(digits):
                ans.append(''.join(path))
                return None
            for i in range(idx,len(digits)):
                for ch in numpad[digits[i]]:
                    # go forward
                    dfs(path+ch,i+1)#pass **i+1**, not idx+1
        # init
        dfs("",0)
        return ans
Solver.solve(Solution,"23")