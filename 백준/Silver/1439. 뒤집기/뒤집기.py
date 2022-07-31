import collections,sys
s=sys.stdin.readline().strip()
zeros = ones = 0
if s[0]=='1': ones +=1
else: zeros +=1
for i in range(len(s)-1):
    if s[i]=='1' and s[i+1]=='0': zeros+=1
    if s[i]=='0' and s[i+1]=='1': ones +=1
sys.stdout.write(str(min((zeros, ones))))