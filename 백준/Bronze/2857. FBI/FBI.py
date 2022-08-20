ans = []
for i in range(5):
    s = input().strip()
    if s.find("FBI")!=-1: ans.append(i+1)
if ans: print(*ans,sep=' ')
else: print("HE GOT AWAY!")