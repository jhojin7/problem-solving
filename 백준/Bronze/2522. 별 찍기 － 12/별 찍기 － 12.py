import sys
n=int(input())
for i in range(1,n):
    for j in range(n-i): 
        sys.stdout.write(' ')
    for j in range(i): 
        sys.stdout.write('*')
    print()
for i in range(n,0,-1):
    for j in range(n-i): 
        sys.stdout.write(' ')
    for j in range(i): 
        sys.stdout.write('*')
    print()