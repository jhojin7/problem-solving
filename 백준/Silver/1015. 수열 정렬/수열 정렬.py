import sys
input = sys.stdin.readline
N = int(input())
listA = list(map(int,input().split()))
arr = []
tmp = sorted(listA)
for i in range(N):
    arr.append((tmp[i],i))
# arr.sort()
# print(N,arr)

ans = []
for x in listA:
    # print(x)
    for i in range(N):
        if arr[i][0] == x:
            # print(arr[i])
            ans.append(arr[i][1])
            arr.pop(i)
            break

print(*ans,sep=' ')