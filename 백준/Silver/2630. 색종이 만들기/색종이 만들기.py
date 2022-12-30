def quads(i1, j1, i2, j2) -> tuple:#(white, blue)
    white = blue = 0
    half_i = (i2+i1)//2
    half_j = (j2+j1)//2
    if i2-i1 == 0 or j2-j1 == 0: return
    mat_quad = [mat[i][j1:j2] for i in range(i1, i2)]
    # backtrack
    size = len(mat_quad)*len(mat_quad[0]) #paper size
    # count local whites and blues
    for r in mat_quad:
        white += r.count('0')
        blue += r.count('1')
    # reset cnt if all cells have same color
    if white == size: 
        return (1,blue)
    elif blue == size: 
        return (white,1)
    # recursion
    quad1 = quads(i1, j1, half_i, half_j)  # I
    quad2 = quads(i1, half_j, half_i, j2)  # II
    quad3 = quads(half_i, j1, i2, half_j)  # III
    quad4 = quads(half_i, half_j, i2, j2)  # IV
    # element-wise tuple sum
    z = tuple(map(sum,zip(quad1,quad2,quad3,quad4)))
    # print(z)
    return z

import sys
N = int(input())
mat = [sys.stdin.readline().split() for i in range(N)]
whites, blues = quads(0, 0, N, N)
print("{}\n{}".format(whites,blues))