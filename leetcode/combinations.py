'''
https://leetcode.com/submissions/detail/688413973/
https://leetcode.com/submissions/detail/688414561/ #pythonic
'''
from __solver import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # pythonic
        # return list(map(list,
        #     itertools.combinations(range(1,n+1),k)))

        def dfs(nums, path):
            # if conditions are met, backtrack
            if k == len(path):
                print(path)
                result.append(path[:])
                return
            
            # https://leetcode.com/problems/permutations/discuss/1968405/python-solution
            for i in range(len(nums)):
                # if num is visited, pass
                if nums[i] in path: continue
                # visit. add to path.
                path.append(nums[i])
                # recursion
                # nums[i:] to omit previous nums
                dfs(nums[i:], path)
                # pop nums[i] since dfs is over
                path.pop()

        nums = range(1,n+1)
        result = []
        dfs(nums,[])
        return result

inputs = [
    # (n=4,k=2),
    (4,2),
    (1,1)
]

for input in inputs:
    n,k = input
    Solver.solve(Solution,n,k)

    # https://docs.python.org/3/library/inspect.html#inspect.Signature.bind
    # sig = inspect.signature(Solution.combine)
    # sig.bind(input)
    # Solver.solve(Solution)