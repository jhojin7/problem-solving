from math import floor
a,b,c = map(int,input().split())
x = a*b/c
y = a/b*c
print(floor(max(x,y)))