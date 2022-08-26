maxcnt = 0
for _ in range(int(input())):
    s = input()
    fo = s.count("for")
    wh = s.count("while")
    maxcnt = max(fo+wh,maxcnt)
print(maxcnt)