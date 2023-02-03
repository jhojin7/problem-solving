arr = [int(input()) for _ in range(6)]
x,y = arr[:4],arr[4:]
ans = sorted(x)[1:]+[sorted(y)[1]]
print(sum(ans))