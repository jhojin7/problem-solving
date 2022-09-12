N=int(input())
arr=list(map(int,input().split()))
# start with first seen 0
try: i=arr.index(0)
except:
    print(0)
    exit()
cnt=0
# 01 12 20
while i<N:
    # print(i)
    if arr[i]==0:
        while i<N and arr[i]!=1: i+=1
    elif arr[i]==1:
        while i<N and arr[i]!=2: i+=1
    elif arr[i]==2:
        while i<N and arr[i]!=0: i+=1
    cnt+=1
print(cnt)