import sys,bisect
input = sys.stdin.readline
T = int(input())
for _ in range(T): 
    a,b = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    # B.sort(reverse=True)
    B.sort()
    # print(A,B)
    # bruteforce?
    cnt = 0
    for i in range(a):
        # find first A>B in B
        idx = bisect.bisect(B,A[i])
        # print(B[idx-1])
        for j in range(idx-1,-1,-1):
            if A[i]>B[j]: cnt+=1
            # else: break
    sys.stdout.write(f"{cnt}\n")