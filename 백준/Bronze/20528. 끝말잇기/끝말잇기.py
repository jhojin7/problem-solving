import sys
input = sys.stdin.readline

n = int(input())
ok = True
palis = list(input().split())
for i,pali in enumerate(palis):
    if i<n-1 and palis[i][-1] != palis[i+1][0]:
        ok = False
        break
    elif pali != pali[::-1]:
        ok = False
        break
if ok==False: print(0)
else: print(1)