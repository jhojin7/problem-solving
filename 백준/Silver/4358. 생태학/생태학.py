import collections
arr = []
while 1:
    try: arr.append(input().strip())
    except: break
cnter = collections.Counter(arr)
n = sum(cnter.values())
# print(n,cnter)
for k,v in sorted(cnter.items()):
    # print(k,round(v/n*100,4))
    print(k,"%.4f"%(v/n*100))