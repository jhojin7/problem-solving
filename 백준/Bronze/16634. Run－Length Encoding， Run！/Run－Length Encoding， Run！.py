import collections
c,s=input().split()
if c=='D':
    for i in range(0,len(s),2):
        print(s[i]*int(s[i+1]),end='')
else:
    i=0
    while i<len(s):
        j=i+1
        cnt=1
        while j<len(s) and s[i]==s[j]:
            j+=1
            cnt+=1
        print(f"{s[i]}{cnt}",end='')
        i=j