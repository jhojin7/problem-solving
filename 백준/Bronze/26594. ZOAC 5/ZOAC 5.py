s=list(input().strip())
c = s.pop()
n=1
while s:
    cc = s.pop()
    if cc==c:
        n+=1
        continue
    else:
        break
print(n)