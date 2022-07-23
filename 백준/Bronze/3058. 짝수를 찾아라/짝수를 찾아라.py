t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    arr = [n for n in arr if n%2==0]
    print(sum(arr),sorted(arr)[0])