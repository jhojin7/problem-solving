import sys
input = sys.stdin.readline
n,k = map(int,input().split())
def f():
    cnt =0
    for i in range(1,n+1):
        if n%i == 0:
            # print(n,i)
            cnt += 1
        if cnt == k:
            print(i)
            return
    print(0)
    return
f()