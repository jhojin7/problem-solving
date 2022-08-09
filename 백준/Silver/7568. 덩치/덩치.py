N=int(input())
arr = []
for _ in range(N):
    x,y=map(int,input().split())
    arr.append((x,y))
rank = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i!=j 
            and arr[i][0]<arr[j][0]
            and arr[i][1]<arr[j][1]):
            rank[i] += 1
for r in rank:
    print(r+1,end=' ')
