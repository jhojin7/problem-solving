import sys; input = sys.stdin.readline
X,Y = map(int,input().split())
def rev(x):
    return int(''.join(reversed(str(x))))
print(rev(rev(X)+rev(Y)))