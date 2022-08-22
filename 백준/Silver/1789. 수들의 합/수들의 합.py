s=int(input())
for n in range(100000):
    if s<(n*(n+1)//2): break
print(n-1)