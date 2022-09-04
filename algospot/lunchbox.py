# https://algospot.com/judge/submission/detail/750346
for _ in range(int(input())):
    N=int(input())
    M=list(map(int,input().split()))
    E=list(map(int,input().split()))
    arr = list(zip(E,M))
    arr.sort(reverse=True)
    print(arr)
    start,end=0,0
    for e,m in arr:
        start+=m
        end=max(end,start+e)
        print(start,end)
    print(end)

# 8? 7??????
# 1
# 2
# 2 1
# 5 1