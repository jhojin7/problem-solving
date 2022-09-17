import collections
T=set([n*(n+1)//2 for n in range(1,1001)])
for _ in range(int(input())):
    n=int(input())
    yes=False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (
                    i+j+k==n
                    and i in T
                    and j in T
                    and k in T): 
                    yes=True
                if yes: break
            if yes: break
        if yes: break
    print(int(yes))