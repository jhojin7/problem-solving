import collections
nn = 50
num = [0 for _ in range(nn)]
num[0]=0
num[1]=1
for k in range(2,nn):
    num[k] = num[k-1]+num[k-2]
# print(num)
for _ in range(int(input())):
    n=int(input())
    nnn = []
    for i in range(len(num)-1,0,-1):
        if n-num[i]>=0:
            nnn.append(num[i])
            n-=num[i]
    # print(n,nnn)
    print(*sorted(nnn))