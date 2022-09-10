for _ in range(int(input())):
    n=int(input())
    arr = []
    for _ in range(n):
        a,b=map(int,input().split())
        arr.append((a,b))
    arr.sort()
    M=arr[0][1]
    cnt=1
    for i in range(1,n):
        if arr[i][1]<M:
            M=arr[i][1]
            cnt+=1
    print(cnt)