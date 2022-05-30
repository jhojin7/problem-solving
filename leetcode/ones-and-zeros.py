"""
"""
import time
from timeit import timeit
from __solver import *
class Solution:
    def notfindMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ans = []
        print(strs,m,n)
        for str in strs:
            cnt = collections.Counter(str)
            print(str,cnt)
            zeros = cnt["0"]
            ones = cnt["1"]
            if zeros<=m and ones<=n:
                ans.append(str)
        print(ans)
        return ans

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        good = []
        for r in range(len(strs),0,-1):
            subsets = itertools.combinations(strs,r)
            print(strs,subsets)
            for subset in subsets:
                joined = ''.join(subset)
                zeros, ones = joined.count('0'), joined.count('1')
                if zeros<=m and ones<=n:
                    print(subset,zeros,ones)
                    # good.append([zeros,ones,list(subset)])
                    good.append(list(subset))
        # good = sorted(good,reverse=True)
        # https://docs.python.org/3/howto/sorting.html#key-functions
        # good.sort(reverse=True, key=lambda subset:len(subset[-1]))
        good.sort(reverse=True)
        print(good,end='\n')
        if len(good)==0: return 0
        return len(good[0])
        # return len(good[0][-1])

# ["10","0001","111001","1","0"]
# 5
# 3
# ["10","0","1"]
# 1
# 1
# ret = Solution().findMaxForm(["10","0001","111001","1","0"],5,3)
# ret = Solution().findMaxForm(["10","0","1"],1,1)
# ret = Solution().findMaxForm(["00","000"],1,10)
# ret = Solution().findMaxForm(["0","0","1","1"],2,2)
# ret = Solution().findMaxForm(["1"],1,2)
strs,m,n = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"],9,80
start_t = time.time()
ret = Solution().findMaxForm(strs,m,n)
print(f"{ret} time {time.time()-start_t}")
