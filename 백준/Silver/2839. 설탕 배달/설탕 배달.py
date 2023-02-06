N=int(input())
cnt =0
s = 99999
for i in range(1001):
    for j in range(1668):
        if 5*i+3*j==N:
            s=min(s,i+j)
if s==99999:print(-1)
else: print(s)