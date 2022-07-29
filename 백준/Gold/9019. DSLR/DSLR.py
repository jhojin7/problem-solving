import sys, collections
input = sys.stdin.readline

def D(n):
    return (2*n)%m

def S(n):
    if n==0: return 9999
    return n-1

def L(n):
    d1 = n//1000
    return (n%1000)*10+d1

def R(n):
    d4 = n%10
    return d4*1000+n//10

def solve(A,B):
    queue = collections.deque([(A,"")])
    visited = set()
    while queue:
        n,ops = queue.popleft()
        if n in visited: continue
        if n==B: return ops
        visited.add(n)
        
        if D(n) not in visited:
            queue.append((D(n),ops+'D'))
        if S(n) not in visited:
            queue.append((S(n),ops+'S'))
        if L(n) not in visited:
            queue.append((L(n),ops+'L'))
        if R(n) not in visited:
            queue.append((R(n),ops+'R'))

t = int(input())
m = 10000
for _ in range(t):
    A,B = map(int,input().split())
    ans = solve(A,B)
    print(ans)