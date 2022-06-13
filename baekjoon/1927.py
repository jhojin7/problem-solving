"""
problem:https://www.acmicpc.net/problem/1927
ac:https://www.acmicpc.net/source/44487244
"""
tc = """
6
1
1
2
0
0
0
"""
import sys
from __boj import BOJ
BOJ(tc)
class minheap:
    def __init__(self) -> None:
        self.heap = []

    def push(self, x):
        added = False
        for i in range(len(self.heap)):
            if self.heap[i] > x:
                self.heap.insert(i,x)
                added = True
                break
        if added == False:
            self.heap.append(x)

    def pop(self):
        if len(self.heap) == 0:
            print(0)
        else:
            print(self.heap[0])
            self.heap.pop(0)

# N = int(input())
# heap = minheap()
# for _ in range(N):
#     x = int(input()) 
#     if x == 0:
#         heap.pop()
#     else:
#         heap.push(x)

import heapq, sys
N = int(sys.stdin.readline())
h = []
result = []
for _ in range(N):
    # print(heap)
    x = int(sys.stdin.readline()) 
    # pop
    if x == 0:
        if len(h) == 0:
            result.append(0)
            # print(0)
        else:
            result.append(heapq.heappop(h))
            # print(heapq.heappop(heap))
    # push
    else:
        heapq.heappush(h,x)
for i in range(len(result)):
    print(result[i])