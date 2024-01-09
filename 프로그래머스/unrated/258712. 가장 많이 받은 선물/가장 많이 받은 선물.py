import collections
def solution(friends, gifts):
    g = collections.defaultdict(list)
    N = len(friends)
    cnt = [[0 for _ in range(N)] for _ in range(N)]
    for ab in gifts:
        a,b = ab.split()
        a,b = friends.index(a), friends.index(b)
        cnt[a][b] +=1
        
    ans = [[0,0,0,0] for _ in range(N)]
    for ab in gifts:
        a,b = ab.split()
        a,b = friends.index(a), friends.index(b)
        ans[a][0] = sum(cnt[a])
    for a in range(N):
        ans[a][1] = sum([cnt[i][a] for i in range(N)])
        ans[a][2] = ans[a][0]-ans[a][1]
    for a in range(N):
        for b in range(a,N):
            if cnt[a][b]!=cnt[b][a]:
                if ans[a][2]==ans[b][2]: continue
                if cnt[a][b]>cnt[b][a]:
                    ans[a][3]+=1
                else:
                    ans[b][3]+=1
            else:
                if ans[a][2]==ans[b][2]: continue
                if ans[a][2] > ans[b][2]:
                    ans[a][3]+=1
                elif ans[a][2] < ans[b][2]:
                    ans[b][3]+=1
    return max([ans[i][3] for i in range(N)])