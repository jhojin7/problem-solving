for i in range(1,int(input())+1):
    print(f"Scenario #{i}:")
    arr = list(map(int,input().split()))
    arr.sort()
    a,b,c=arr
    if a*a+b*b==c*c: print("yes")
    else: print("no")
    print()