def solve():
    # a,b = map(int,input().split())
    # return (a+b)%24
    return sum(list(map(int,input().split())))%24

# for i in range(1,11):
for i in range(1,int(input())+1):
    print(f"#{i} {solve()}")