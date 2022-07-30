cnt = 0
n = int(input())
for _ in range(n):
    s = list(input().strip())
    # print(s)
    i = 0
    visited = set()
    nope = False
    while i<len(s):
        if s[i] in visited:
            nope = True
            break
        visited.add(s[i])
        while i+1<len(s) and s[i]==s[i+1]: i+=1
        i+=1
    if not nope: cnt+=1
    # print(i,visited)
print(cnt)
