while 1:
    arr = list(map(int,input().split()))
    if arr==[0,0,0]: break
    a,b,c = sorted(arr)
    if a+b<=c: print("Invalid")
    elif a==b==c: print("Equilateral")
    elif a==b or b==c or c==a: print("Isosceles")
    elif a!=b!=c: print("Scalene")