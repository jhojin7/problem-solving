import itertools
X=input().strip()

comb = list(itertools.permutations(X,len(X)))
comb.sort()
# print(comb)
ans = None
for com in comb:
    n = int(''.join(com))
    if n>int(X):
        ans = n
        break
if not ans: print(0)
else: print(ans)