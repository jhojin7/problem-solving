N,m=map(int,input().split())
K = []
for _ in range(m):
    K.append(int(input()))
K.sort()
# print(K)
cnt=0
for k in K:
    if N-k>=0:
        cnt+=1
        N-=k
print(cnt)