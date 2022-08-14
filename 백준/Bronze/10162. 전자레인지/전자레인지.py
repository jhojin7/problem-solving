t=int(input())
# 5min 1min 10sec
x = t//60
y = x%5
x = x//5
t%=60
z = t//10
t%=10
if t!=0: print(-1)
else: print(x,y,z)