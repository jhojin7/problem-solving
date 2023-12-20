arr = input().split('-')
ans = 0
if len(arr) == 1:
    print(sum(list(map(int, arr[0].split('+')))))
    exit()

ans += sum(list(map(int, arr[0].split('+'))))
for s in arr[1:]:
    if '+' in s:
        ans -= sum(list(map(int, s.split('+'))))
    else:
        ans -= int(s)
print(ans)
