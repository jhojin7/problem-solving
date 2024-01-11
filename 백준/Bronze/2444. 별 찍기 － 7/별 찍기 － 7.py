N = int(input())

ans = []
for i in range(1, N*2, 2):
    tmp = []
    tmp.extend([' ' for _ in range((2*N-i)//2)])
    tmp.extend(['*' for _ in range(i)])
    # tmp.extend([' ' for _ in range((N-i))])
    ans.append(tmp)
ans2 = []
for i in range(1, N*2-1, 2):
    tmp = []
    tmp.extend([' ' for _ in range((2*N-i)//2)])
    tmp.extend(['*' for _ in range(i)])
    # tmp.extend([' ' for _ in range((N-i))])
    ans2.append(tmp)
ans.extend(reversed(ans2))

for a in ans:
    print(*a, sep='')
