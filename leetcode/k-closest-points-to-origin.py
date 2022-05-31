"""
https://leetcode.com/submissions/detail/711102138/
"""
from __solver import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x,y in points:
            # find euclidian distance
            euc_dist = math.sqrt(x**2+y**2)
            heapq.heappush(pq,(euc_dist,x,y))
        # pop k elements
        ans = []
        for _ in range(k):
            _,x,y = heapq.heappop(pq)
            ans.append((x,y))
        return ans
points,k = [[1,3],[-2,2]],1
# points,k = [[3,3],[5,-1],[-2,4]],2
print(Solution().kClosest(points,k))