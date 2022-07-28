import sys,math
l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
ac=math.ceil(a/c)
bd=math.ceil(b/d)
print(l-max(ac,bd))