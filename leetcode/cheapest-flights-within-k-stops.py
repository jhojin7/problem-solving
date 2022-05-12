"""
time limit
https://leetcode.com/submissions/detail/698084239/
https://github.com/onlybooks/algorithm-interview/issues/104
"""
from __solver import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = 0
        # graph init
        graph = collections.defaultdict(list)
        for frm,to,price in flights:
            print(frm,to,price)
            graph[frm].append((to, price))
        print(graph)

        # pqueue for traversing (price, city, k)
        Q = [(0,src,k)] # starting point
        while Q:
            price, city, k = heapq.heappop(Q)
            # if current city is destination, return tot price
            if city==dst:
                print(price)
                return price
            # while k stops > 0, visit other connected cities
            if k >=0:
                for _to,_price in graph[city]:
                    heapq.heappush(Q,(price+_price,_to,k-1))
        # if no such route
        return -1


inputs = [
    4,
    [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    ,0,3,1
    ,3,
    [[0,1,100],[1,2,100],[0,2,500]]
    ,0,2,1
    ,3,
    [[0,1,100],[1,2,100],[0,2,500]]
    ,0,2,0
]
Solution.findCheapestPrice(Solution, 4,inputs[1],0,3,1)

