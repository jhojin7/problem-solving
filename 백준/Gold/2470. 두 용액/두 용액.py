N = int(input())
arr = sorted(map(int, input().split()))
# print(arr)
l, r = 0, len(arr) - 1
ans = 9 ** 999
ll, rr = -99, -99
while l < r:
    tmp = arr[l] + arr[r]
    # print(l, r, arr[l] + arr[r])
    if abs(tmp) <= abs(ans):
        ans = tmp
        ll, rr = l, r
    if tmp < 0:
        l += 1
    else:
        r -= 1
print(arr[ll], arr[rr])