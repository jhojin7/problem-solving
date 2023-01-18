N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper[i][j] = 1
    
cnt =0
for row in paper:
    cnt+=row.count(1)
print(cnt)