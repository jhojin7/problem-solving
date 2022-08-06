import sys
input = sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
if N<=2:
    print(max(A))
    exit()

maxans = -999999
B = [A[0]]
for i in range(1,len(A)-1):
    if A[i]==0: 
        B.append(A[i])
        continue
    x = min(A[i-1]+A[i],A[i]+A[i+1])
    B.append(x)
    # maxans = max(maxans,x)
B.append(A[-1])
# print(B)
print(max(B))