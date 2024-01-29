K = int(input())
arr = []
x, y = 0, 0
for _ in range(6):
    a, b = map(int, input().split())
    arr.append((a, b))
    if a in [1, 2]:
        x += b
    if a in [3, 4]:
        y += b
x //= 2
y //= 2
aa = [a for a, _ in arr]
aa += [aa[0]]
arr += [arr[0]]
area = x*y
yes = True
todel = 0
for i in range(len(aa)-1):
    comb = ''.join(map(str, aa[i:i+2]))
    if comb in ["13", "41", "24", "32"]:
        todel = arr[i][1]*arr[i+1][1]
        break
print((area-todel)*K)
