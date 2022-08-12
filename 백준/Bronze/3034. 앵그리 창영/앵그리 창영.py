N,W,H = map(int,input().split())
for _ in range(N):
    x = int(input())
    if min(W,H)>=x or x*x<=(W*W+H*H):
        print("DA")
    else:
        print("NE")
