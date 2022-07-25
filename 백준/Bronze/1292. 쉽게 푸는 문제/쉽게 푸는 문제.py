arr = [0 for _ in range(1001)]
n = 1
i = 0
while i<1000:
    for _ in range(n):
        arr[i] = n
        if i==1000: break
        i+=1
    n += 1
A,B=map(int,input().split())
print(sum(arr[A-1:B]))