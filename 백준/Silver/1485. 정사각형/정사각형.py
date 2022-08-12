import collections,math
def dist(pa:tuple,pb:tuple)->tuple:
    return math.sqrt(
        (pa[0]-pb[0])*(pa[0]-pb[0])+
        (pa[1]-pb[1])*(pa[1]-pb[1])
    )

for _ in range(int(input())):
    ans = True
    arr = []
    for _ in range(4):
        x,y = map(int,input().split())
        arr.append((x,y))
    p1,p2,p3,p4 = sorted(arr,reverse=True)
    # print(p1,p2,p3,p4)
    dists = [dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),
             dist(p2,p4),dist(p3,p4)]

    try: 
        dic = collections.Counter(dists)
        edge,diag = sorted(dic.items())
        if not (edge[1]==4 and diag[1]==2):
            ans = False
    except: ans = False

    if ans: print(1)
    else:print(0)