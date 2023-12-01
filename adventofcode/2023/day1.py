lines = []
while 1:
    try:
        lines.append(input())
    except:
        break
# print(lines)

strnums = "zero one two three four five six seven eight nine".split()
d = {}
for k, v in enumerate(strnums, 0):
    d[k] = v
ans = 0
for line in lines:
    tmpline: str = line
    tmp = []
    for i in range(len(line)):
        if line[i] in "123456789":
            tmp.append((i, line[i]))
        else:
            for k, v in d.items():
                if v in line[i:i+len(v)]:
                    tmp.append((i, k))

    tmp.sort()
    a = tmp[0][1]
    b = tmp[-1][1]
    print(tmp, int(a)*10+int(b))
    ans += int(a)*10+int(b)
print(ans)

"""
nineightwo
threeightwone
92?93?
"""
