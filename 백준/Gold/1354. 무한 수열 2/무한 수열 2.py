import collections
N,P,Q,X,Y= map(int,input().split())
A = collections.defaultdict(int)
def calc(i):
    if i<=0:
        A[0]=1
        return 1
    else:
        if A[i]!=0: return A[i]
        A[i] = calc(i//P-X)+calc(i//Q-Y)
        return A[i]
print(calc(N))