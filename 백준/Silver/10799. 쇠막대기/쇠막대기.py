s = input().strip()
s = s.replace("()", "x")
pipe = 0
ans = 0
for c in s:
    if c == '(':
        pipe += 1
    elif c == 'x':
        ans += pipe
    else:
        ans += 1
        pipe -= 1
print(ans)
