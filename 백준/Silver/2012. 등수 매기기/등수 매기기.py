N=int(input())
A,B=[],[]
for _ in range(N):
    A.append(int(input()))
A.sort()
B=list(range(1,N+1))
ans=0
for a,b in zip(A,B):
    # print(a,b,abs(a-b))
    ans+=abs(a-b)
print(ans)