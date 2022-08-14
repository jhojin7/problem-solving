a,b = input().split()
c = a.replace('5','6')
d = b.replace('5','6')
e = a.replace('6','5')
f = b.replace('6','5')
maxij = -9999999
minij = 9999999
for i in [a,c,e]:
    for j in [b,d,f]:
        maxij = max(int(i)+int(j),maxij)
        minij = min(int(i)+int(j),minij)
print(minij,maxij)