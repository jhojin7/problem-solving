arr = []
for _ in range(int(input())):arr.append(tuple(map(int,input().split())))
for x,y in sorted(arr,key=lambda x:(x[1],x[0])): print(x,y)