N = int(input())
ans = 100000
for i in range(5000//3+1):
    for j in range(5000//5+1):
        if 3*i+5*j > N:
            break
        elif 3*i+5*j == N:
            ans = min(ans, i+j)
if ans == 100000:
    print(-1)
else:
    print(ans)
