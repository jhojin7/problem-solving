import collections
d = collections.defaultdict(int)
d[0]=1
def t(n):
    if d[n]!=0: return d[n]
    tmp =0
    for i in range(n):
        tmp+=t(i)*t(n-i-1)
    d[n] = tmp
    return d[n]
n=int(input())
print(t(n))