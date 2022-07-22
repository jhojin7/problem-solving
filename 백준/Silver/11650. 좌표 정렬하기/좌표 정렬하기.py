arr = []
for _ in range(int(input())):
    arr.append(tuple(map(int,input().split())))
arr.sort()
for x,y in arr: print(x,y)