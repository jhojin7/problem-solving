hh,mm = map(int,input().split())
mins = int(input())
tttt=hh*60+mm+mins
h = tttt//60
m = tttt%60
if h>=24: h-=24
print(h,m)
