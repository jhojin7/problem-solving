a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
xor = A^B
print(len(xor))