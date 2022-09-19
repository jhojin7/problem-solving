s=input().strip()
t=[]
alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in s:
    i = (alpha.index(c)-3)%len(alpha)
    t.append(alpha[i])
print(''.join(t))