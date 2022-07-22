N = int(input());arr = []
for _ in range(N):
    age,namee = input().split()
    arr.append((int(age),namee))
arr.sort(key=lambda x:(x[0]))
for x in arr: print(*x,sep=' ')