import sys
input = sys.stdin.readline

def zzz(minval, maxval, edge1, edge2):
    (i1, j1), (i2, j2) = edge1, edge2
    half = (minval+maxval)//2
    # print(minval, maxval,edge1,edge2)
    if edge1 == (r,c):
        return minval
    elif minval+1 == maxval: return -1

    half_i = (i1+i2)//2
    half_j = (j1+j2)//2
    if i1<=r<half_i and j1<=c<half_j:
        return zzz(minval, (minval+half)//2, edge1, (half_i, half_j))
    elif i1<=r<half_i and half_j<=c<j2:
        return zzz((minval+half)//2, half, (i1, half_j), (half_i, j2))
    elif half_i<=r<i2 and j1<=c<half_j:
        return zzz(half, (half+maxval)//2, (half_i, j1), (i2, half_j))
    elif half_i<=r<i2 and half_j<=c<j2:
        return zzz((half+maxval)//2, maxval, (half_i, half_j), edge2)
    else:
        return -1

N, r, c = map(int, input().split())
Nsq = 2**N
print(zzz(0, Nsq*Nsq, (0, 0), (Nsq, Nsq)))