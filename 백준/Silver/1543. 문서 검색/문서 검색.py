import sys
input = sys.stdin.readline
s=input().strip()
t=input().strip()
l,r = 0,len(t)
cnt = 0
while r<=len(s):
    # print(s[l:r])
    if s[l:r]==t: 
        cnt+=1
        l = r
        r = r+len(t)
    else:
        l+=1
        r+=1
print(cnt)