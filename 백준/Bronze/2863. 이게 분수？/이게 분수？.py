a,b = map(int,input().split())
c,d = map(int,input().split())
arr = [[a,b],[c,d]]

def rotate(arr):
    a,b = arr[0]
    c,d = arr[1]
    return [[c,a],[d,b]]

def calc(arr):
    a,b = arr[0]
    c,d = arr[1]
    return a/c+b/d

a1 = calc(arr),
a2 = calc(rotate(arr)),
a3 = calc(rotate(rotate(arr))),
a4 = calc(rotate(rotate(rotate(arr)))),
ans = zip([a1,a2,a3,a4],[0,1,2,3])
print(max(ans)[1])