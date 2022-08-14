from math import pi
a1,p1=map(int,input().split())
r1,p2=map(int,input().split())
x=a1/p1
y=(pi*r1*r1)/p2
if x<y: print("Whole pizza")
else: print("Slice of pizza")