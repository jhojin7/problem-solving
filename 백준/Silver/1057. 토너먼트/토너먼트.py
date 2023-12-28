n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

ans = 1
# while a and b:
while a > 1 and b > 1:
    # print(a, b, ans)
    a, b = min(a, b), max(a, b)
    if a+1 == b and a % 2 == 1 and b % 2 == 0:
        print(ans)
        exit()
    a = a//2 if a % 2 == 0 else (a+1)//2
    b = b//2 if b % 2 == 0 else (b+1)//2
    ans += 1
if a+1 == b:
    print(ans)
    exit()
while b > 1 and a+1 != b:
    # print(a, b, ans)
    a, b = min(a, b), max(a, b)
    a = a//2 if a % 2 == 0 else (a+1)//2
    b = b//2 if b % 2 == 0 else (b+1)//2
    ans += 1
if a+1 == b:
    print(ans)
    exit()
print(ans)
