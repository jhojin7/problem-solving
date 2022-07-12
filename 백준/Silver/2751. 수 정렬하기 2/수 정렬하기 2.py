import sys,heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap,int(input()))
for _ in range(N):
    print(heapq.heappop(heap))