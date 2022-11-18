import itertools

N=int(input())
arrr = list(range(N))
arr = []
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

def team(nums):
    ret = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            x,y = nums[i],nums[j]
            ret+=arr[x][y]+arr[y][x]
    return ret

ans = 99999999
for r in range(2,N//2+1):
    combs = itertools.combinations(range(N),r)
    for comb in combs:
        comb2 = set(range(N))-set(comb)
        # print(comb,comb2)
        team1 = team(list(comb))
        team2 = team(list(comb2))
        ans = min(ans,abs(team1-team2))
print(ans)