"""
https://leetcode.com/submissions/detail/715517524/
"""
from __solver import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if no cooldown, return len(tasks)
        if n == 0: return len(tasks)
        #####
        times = 0
        counter = collections.Counter(tasks)
        while counter:
            # print(counter.most_common(n+1))
            # counter to check if n numbers are popped
            m = 0
            for task,_ in counter.most_common(n+1):
                # counter[task] -= 1
                counter.subtract(task)
                # mask over elements with value=0
                counter += collections.Counter()
                # print(task, counter)

                # increment subcounter and times 
                m += 1
                times += 1
            # if finished counting, return times
            if not counter:
                break
            # print(".", counter)
            # increment times
            times+=1 + (n-m)
        return times

# tasks, n = ["A","A","A","B","B","B"],0
tasks, n = ["A","A","A","B","B","B"],2
# tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"],2#16
print(Solution().leastInterval(tasks,n))