class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        ans = []
        def dfs(path, idx):
            print(path, idx)
            # stop recursion
            if len(path) == len(nums):
                ans.append(path)
                print(f"ret {path}")
                #ans += path
                return
            # do dfs
            for i in range(idx,len(nums)):
                # visit new num and move idx+1
                #if i != idx: 
                dfs(path+[nums[i]],idx+1)
        # main
        dfs([],0)
        print(ans)
        return ans