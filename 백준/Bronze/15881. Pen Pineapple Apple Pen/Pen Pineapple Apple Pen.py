# pPAp
n=int(input())
s=list(input().strip())
cnt=0
for i in range(len(s)-3):
    if list("pPAp")==s[i:i+4]: 
        cnt+=1
        s[i]='_'
        s[i+3]='_'
print(cnt)