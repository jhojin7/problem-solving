import sys
input = sys.stdin.readline
N = int(input())
s = list(input().strip())
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0
idxes = []
for i in range(1,len(s)-1):
    c1 = capitals.index(s[i-1])
    c2 = capitals.index(s[i])
    c3 = capitals.index(s[i+1])
    diff1 = abs(c1-c2)
    diff2 = abs(c2-c3)
    # print(s[i-1],s[i],s[i+1])
    # print(idxes)
    # print(i,diff1,diff2)
    if diff1==1 and diff2==1:
    # if diff1>0 and diff2>0 and diff1==diff2:
        if idxes and idxes[-1]!=i-1:
            idxes = [i]
        else:
            idxes.append(i)
    if len(idxes)>=3:
        break

# print(idxes)
if len(idxes)<3: print("NO")
else: print("YES")