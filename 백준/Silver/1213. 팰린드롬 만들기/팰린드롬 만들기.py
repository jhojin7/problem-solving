import collections
s=input()
cnter=collections.Counter(s)
# print(cnter)
evens,odds=[],[]
for k,v in cnter.items():
    if v%2==0: evens.append(k)
    else: odds.append(k)
# print(evens,odds)
if len(odds)>1:
    print("I'm Sorry Hansoo")
    exit()
ans=[]
for k in sorted(cnter.keys()):
    ans.append(k*(cnter[k]//2))
    cnter[k]%=2
if odds: o=odds[0]
else: o=''
print("".join([*ans,o,*ans[::-1]]))