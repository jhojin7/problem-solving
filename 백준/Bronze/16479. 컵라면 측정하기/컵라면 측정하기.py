import math
k=int(input())
d1,d2=map(int,input().split())
tri_w = (d1-d2)/2
hsq = k*k-tri_w*tri_w
print(hsq)