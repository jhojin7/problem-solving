n=int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
nums = set(list(range(1,n*n+1)))
for i in range(n):
    for j in range(n):
        try:nums.remove(mat[i][j])
        except: 
            print("FALSE")
            exit()
if len(nums)!=0:
    print("FALSE")
    exit()

s = n*(n*n+1)//2
for row in mat:
    if sum(row)!=s:
        print("FALSE")
        exit()
for j in range(n):
    if sum([mat[i][j] for i in range(n)])!=s:
        print("FALSE")
        exit()
x1,x2=0,0
for i in range(n):
    x1+=mat[i][i]
    x2+=mat[i][n-i-1]
if x1!=s or x2!=s:
    print("FALSE")
    exit()
print("TRUE")