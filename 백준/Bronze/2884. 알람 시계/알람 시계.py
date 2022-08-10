h,m = map(int,input().split())
t = h*60+m-45
hh,mm = t//60,t%60
if hh<0: hh += 24
print(hh,mm)