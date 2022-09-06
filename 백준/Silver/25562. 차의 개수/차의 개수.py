N=int(input())
#max
print(N*(N-1)//2)
diff=0
for _ in range(N):
    print(1+diff,end=' ')
    diff+=diff+1
print()
#min
print(N-1)
for n in range(1,N+1):
    print(n,end=' ')