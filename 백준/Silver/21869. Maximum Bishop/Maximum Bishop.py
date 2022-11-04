N=int(input())
m = N//2
# print(m)
ans=[]
for j in range(N):
    # print(1,j+1)
    ans.append((1,j+1))
for j in range(1,N-1):
    # print(m+1,j+1)
    ans.append((N,j+1))

print(len(ans))
for a in ans:
    print(*a)