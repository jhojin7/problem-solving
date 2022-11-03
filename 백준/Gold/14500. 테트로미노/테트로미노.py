shapes = [
    # -
    [[1,1,1,1]],
    [[1],[1],[1],[1]],
    # ㅁ
    [[1,1],[1,1]],
    # ㄴ
    [[1,0],[1,0],[1,1]],
    [[1,1,1],[1,0,0]],
    [[1,1],[0,1],[0,1]],
    [[1,0,0],[1,1,1]],
    # ㄴㄴ
    [[0,1],[0,1],[1,1]],
    [[1,1,1],[0,0,1]],
    [[1,1],[1,0],[1,0]],
    [[0,0,1],[1,1,1]],
    # ㄴㄱ
    [[1,0],[1,1],[0,1]],
    [[0,1],[1,1],[1,0]],
    [[0,1,1],[1,1,0]],
    [[1,1,0],[0,1,1]],
    # ㅗ
    [[0,1,0],[1,1,1]],
    [[1,1,1],[0,1,0]],
    [[1,0],[1,1],[1,0]],
    [[0,1],[1,1],[0,1]],
]
shapes.sort(key=lambda x:len(x))

N,M = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

def tetromino(shape,x,y):
    w,h = len(shape[0]),len(shape)
    ret = 0
    for i in range(h):
        for j in range(w):
            if shape[i][j]:
                ret += grid[x+i][y+j]
    return ret
# ret = tetromino(shapes[0],4,0)

maxsco = 0
for shape in shapes:
    w,h = len(shape[0]),len(shape)
    for i in range(N):
        for j in range(M):
            if i+h>N or j+w>M: continue
            # print(shape,i,j)
            maxsco = max(maxsco,tetromino(shape,i,j))
print(maxsco)
