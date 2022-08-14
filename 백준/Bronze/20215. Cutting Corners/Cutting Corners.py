import math
w,h=map(int,input().split())
rect = w+h
diag = math.sqrt(w*w+h*h)
print(rect-diag)