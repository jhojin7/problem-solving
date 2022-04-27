'''
https://leetcode.com/submissions/detail/688394773/
'''
from __solver import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # pythonic
        # return list(map(list,itertools.permutations(nums)))

        # DFS
        # def dfs(nums, path):
        #     if len(path) == len(nums):
        #         # deep copy
        #         result.append(path[:])
        #         return
        #     # define not_visited
        #     visit = nums[0]
        #     not_visited = nums[1:]
        #     # visit a num
        #     path.append(visit)
        #     # go down the dfs tree
        #     for num in not_visited:
        #         # append visited number to path
        #         print(num, path, not_visited, result)
        #         dfs(nums, path)

        def dfs(nums, path):
            # if full, appennd to result
            if len(nums) == len(path):
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
                dfs(nums, path)
                # pop nums[i] since dfs is over
                path.pop()

            # # define not_visited
            # # visit leftmost num and add to path
            # path.append(nums[idx])
            # # and remove from not_visited
            # idx += 1
            # # for every num in not_visited
            # #     dfs(nums,not_visited,path)
            # for n in range(idx,len(nums)):
            #     print(nums, path, idx, nums[n:len(nums)])
            #     dfs(nums, path, idx)

        result = []
        dfs(nums,[])
        return result

inputs = [
[1,2,3]
,[0,1]
,[1]
]
for inp in inputs:
    Solver.solve(Solution,inp)