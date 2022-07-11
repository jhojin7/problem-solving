import sys,collections
input = sys.stdin.readline

N,M = map(int,input().split())
mat,visited = [],[]
for _ in range(N):
    visited.append([[False for _ in range(2)] for _ in range(M)])
for _ in range(N):
    mat.append(list(map(int,input().strip())))

def can_visit(i,j):
    if not(1<=i+1<=N and 1<=j+1<=M): return False
    if mat[i][j] == 1: return False
    return True

def bfs():
    queue = collections.deque([(0,0,1,0)])
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    
    while queue:
        i,j,dist,broken_wall = queue.popleft()

        # visit
        if visited[i][j][broken_wall]: continue
        visited[i][j][broken_wall] = True 
        if (i,j) == (N-1,M-1):
            return dist
        
        for di,dj in directions:
            next_ij1 = (i+di,j+dj)
            next_ij2 = (i+di*2,j+dj*2)
            # if wall not yet broken
            if broken_wall == 0:
                if can_visit(*next_ij1):
                    queue.append((*next_ij1,dist+1,broken_wall))
                if not can_visit(*next_ij1) and can_visit(*next_ij2):
                    queue.append((*next_ij2,dist+2,1))
            # if wall broken previously
            elif broken_wall == 1:
                if can_visit(*next_ij1):
                    queue.append((*next_ij1,dist+1,broken_wall))
            else:
                print("????")
    return -1
print(bfs())