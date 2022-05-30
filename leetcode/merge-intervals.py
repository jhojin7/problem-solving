"""
https://leetcode.com/submissions/detail/710667397/
"""
from __solver import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        ans = []
        print(intervals)
        for i in range(len(intervals)):
            # if last known interval can merge with current interval, merge
            if ans and ans[-1][1] >= intervals[i][0]:
                # choose between prev[1] or cur[1]
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
            else:
                ans.append(intervals[i])
        print(ans)
        return ans
intervals = [[1,3],[8,10],[2,6],[15,18]]
intervals = [[4,5],[1,4]]
intervals = [[1,4],[2,3]]
Solution().merge(intervals)