y = set("YONSEI".strip())
k = set("KOREA".strip())

s = list(input())
for c in s:
    if c in y:
        y.remove(c)
    if c in k:
        k.remove(c)
    if not k:
        print("KOREA")
        exit()
    if not y:
        print("YONSEI")
        exit()