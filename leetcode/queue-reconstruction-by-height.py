"""
https://leetcode.com/submissions/detail/716304244/
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/1169017/Python-Concise-Simple-and-Understand-able-Solution 
"""
from __solver import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
            # sort people by reverse h order
            # and by k order
            people.sort(key=lambda ppl:(-ppl[0],ppl[1]))
            # queue[j] = [h,k] where 
            # h=height, k=people cnt in front
            queue = []
            for x in people:
                # insert at k position
                queue.insert(x[1], x)
            return queue

tc = testcases("""
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
""")

while tc:
    args = tc.popleft()
    print(Solution().reconstructQueue(*args))