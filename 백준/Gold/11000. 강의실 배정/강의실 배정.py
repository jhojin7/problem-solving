import heapq

N=int(input())
arr=[]
for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
# arr.sort(key=lambda x:x[1])
arr.sort()
# print(arr)
pq=[arr[0][1]]
for st,fin in arr[1:]:
    if st < pq[0]:
        heapq.heappush(pq,fin)
    else:
        heapq.heappop(pq)
        heapq.heappush(pq,fin)
print(len(pq))