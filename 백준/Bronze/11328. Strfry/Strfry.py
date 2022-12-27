for _ in range(int(input())):
    a,b = input().split()
    if sorted(a)==sorted(b):
        print("Possible")
    else:
        print("Impossible")