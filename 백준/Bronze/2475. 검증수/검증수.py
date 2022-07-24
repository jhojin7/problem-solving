arr = list(map(int,input().split()));s=0
for a in arr:s += a*a
print(s%10)