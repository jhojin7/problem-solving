N,M,B = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

ansh,anst=9999999999,99999999999
for h in range(257):
    rem,add=0,0
    for i in range(N):
        for j in range(M):
            diff = grid[i][j]-h
            if diff>0: rem+=diff
            elif diff<0: add-=diff
    
    if rem+B>=add:
        t = rem*2+add
        if anst>=t: 
            anst=t
            ansh=h
print(anst,ansh)