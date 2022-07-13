T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1,n+1)]
    for f in range(k):
        for i in range(1,len(floor)):
            floor[i] = floor[i-1]+floor[i]
    print(floor[-1])