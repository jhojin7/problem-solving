n=int(input())
for _ in range(n//2):
    print("* "*n)
    print(" *"*n)
if n%2==1:
    print("* "*n)