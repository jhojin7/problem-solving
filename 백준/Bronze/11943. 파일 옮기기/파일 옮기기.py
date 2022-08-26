a,b=map(int,input().split())
c,d=map(int,input().split())
# apple to 1
a1 = c+b
# apple to 2
a2 = a+d
# orange to 1
o1 = d+a
# orange to 2
o2 = b+c
print(min(a1,a2,o1,o2))