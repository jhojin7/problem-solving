N,M = map(int,input().split())
no = set()
for _ in range(M):
    a,b = map(int,input().split())
    no.add(tuple(sorted([a,b])))
cnt = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if ((i,j) in no
                or (j,k) in no
                or (i,k) in no):
                continue
            else:
                cnt+=1
print(cnt)