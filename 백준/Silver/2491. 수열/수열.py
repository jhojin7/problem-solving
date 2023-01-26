import sys,collections, heapq,math
input = sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
ans1,ans2=1,1
cnt=1
for i in range(1,N):
    if arr[i-1]<=arr[i]:
        cnt+=1
    else:
        if i==1: cnt+=1
        ans1=max(ans1,cnt)
        cnt=1
cnt=1
for i in range(1,N):
    if arr[i-1]>=arr[i]:
        # print(arr[i-1],arr[i])
        cnt+=1
    else:
        if i==1: cnt+=1
        ans2=max(ans2,cnt)
        cnt=1
ans1=max(ans1,cnt)
ans2=max(ans2,cnt)
# print(ans1,ans2)
print(max(ans1,ans2))