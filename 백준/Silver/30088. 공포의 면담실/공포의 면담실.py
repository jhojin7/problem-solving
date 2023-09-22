arr = []
for _ in range(int(input())):
    n, *brr = map(int, input().split())
    # arr.append(brr)
    arr.append(sum(brr))
# arr.sort(key=lambda x: sum(x))
arr.sort()
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
# print(arr)
print(sum(arr))