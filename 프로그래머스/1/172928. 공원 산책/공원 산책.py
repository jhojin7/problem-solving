def solution(park, routes):
    curx,cury = 0,0
    park = [list(row.strip()) for row in park]
    #print(park)
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                curx,cury = i,j
    for route in routes:
        #print(route)
        print(curx,cury)
        op, n = route.split()
        n = int(n)
        dxy = {
            'E':(0,1),
            'W':(0,-1),
            'S':(1,0),
            'N':(-1,0),
        }
        dx,dy = dxy[op]
        nx,ny = curx,cury
        abort=False
        for _ in range(n):
            if not (0<=nx<len(park) and 0<=ny<len(park[0])):
                abort=True
                break
            if park[nx][ny]=='X':
                abort=True
                break
            nx,ny = nx+dx, ny+dy
        if not (0<=nx<len(park) and 0<=ny<len(park[0])):
            abort=True
        if not abort and park[nx][ny]=='X':
            abort=True
        if abort:
            continue
        curx,cury = nx,ny
        print(route, curx,cury)
    return [curx,cury]
        
        