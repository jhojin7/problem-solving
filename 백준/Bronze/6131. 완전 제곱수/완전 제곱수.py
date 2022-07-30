N = int(input())
cnt = 0
for a in range(1,501):
    for b in range(1,501):
        if a*a-b*b==N:
            cnt+=1
print(cnt)