s=input()
t="UCPC"
j=0
for i in range(len(s)):
    if s[i]==t[j]: j+=1
    if j==4: break
if j==4: print("I love UCPC")
else: print("I hate UCPC")