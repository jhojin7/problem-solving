'''
https://leetcode.com/submissions/detail/687990310/
'''
from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        make a dict of num and chars
        for digit in digits: 
            for ch in chars:
        '''

        # dfs should take all paths, not 1 char
        def dfs(idx,visited):
            # if requirement met, finish
            if len(digits) == len(visited):
                combos.append(visited)
                return
            
            # else traverse all options
            # from current idx to end
            for i in range(idx,len(digits)): 
                for ch in letters[digits[i]]:
                    # add current ch to visited
                    # and move to next idx
                    dfs(i+1,visited+ch)

        letters = {'2':'abc','3':'def',
        '4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}
        combos = []

        # empty digits
        if digits == "":
            return []

        dfs(0,"")
        return combos

if __name__=='__main__':
    inputs = [
    "23"
    ,""
    ,"2"
    ]
    from __solver import Solver
    for input in inputs:
        Solver.solve(Solution,input)