N,B = map(int,input().split())
alnum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = []
while N>0:
    # print(N%B,alnum[N%B])
    ans.append(alnum[N%B])
    N= N//B
ans.reverse()
print("".join(ans))