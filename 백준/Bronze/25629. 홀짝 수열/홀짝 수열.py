N=int(input())
a=list(map(int,input().split()))
even,odd=[],[]
for x in a:
    if x%2==0: even.append(x)
    else: odd.append(x)
# print(even,odd, len(even),len(odd))
if (len(even)+len(odd)==N 
    and (len(odd)==len(even) or len(odd)==len(even)+1)):
    print(1)
else:
    print(0)