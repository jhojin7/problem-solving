"""
https://leetcode.com/submissions/detail/715454160/
"""
from __solver import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if there's not enough gas to travel all stations,
        # return -1
        if sum(gas) < sum(cost): 
            return -1
        # start == index where current station 
        # has enough gas to go to next station   
        start, fuel = 0, 0
        for i in range(len(gas)):
            # if NOT enough gas to go to next station
            if gas[i] + fuel < cost[i]:
                # set next index as start
                start = i+1 
                # reset fuel
                fuel = 0
            # update fuel
            else:
                fuel += gas[i]-cost[i]
        return start
gas,cost = [1,2,3,4,5],[3,4,5,1,2]#3
gas, cost = [2,3,4],[3,4,3]
gas, cost = [5,1,2,3,4],[4,4,1,5,1] #4
gas,cost = [5,8,2,8],[6,5,6,6] #3
print(Solution().canCompleteCircuit(gas, cost))