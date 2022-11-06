c=input().strip()
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ilove = "ILOVEYONSEI"
ans = 0
# for i in range(len(ilove)):
for ch in ilove:
    cur = chars.index(c)
    nex = chars.index(ch)
    ans+=abs(cur-nex)
    # print(c,ans)
    c = ch
print(ans)