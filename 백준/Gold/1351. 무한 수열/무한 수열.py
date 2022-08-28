import collections
N,P,Q = map(int,input().split())
A = collections.defaultdict(int)
A[0] = 1
def calc(i):
    if A[i]!=0: return A[i]
    A[i] = calc(i//P)+calc(i//Q)
    return A[i]
print(calc(N))