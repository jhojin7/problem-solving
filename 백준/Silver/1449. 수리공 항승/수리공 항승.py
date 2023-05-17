import sys; input = sys.stdin.readline

N,L = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

ans=0
l = arr[0]
for i in range(1,N):
    diff = arr[i]-l
    if diff>=L: 
        ans+=1
        l = arr[i]
print(ans+1)