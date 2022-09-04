# https://algospot.com/judge/submission/detail/750361
import heapq
for _ in range(int(input())):
    n=int(input())
    lens=list(map(int,input().split()))
    lens.sort()
    # print(n,lens)
    ans=0
    heapq.heapify(lens)
    while len(lens)>1:
        l1=heapq.heappop(lens)
        l2=heapq.heappop(lens)
        # print(l1,l2)
        ans+=l1+l2
        heapq.heappush(lens,l1+l2)
    print(ans)