n=int(input())
o,p = 0,0
while n%2!=1:
    n = n//2
    p+=1
o = n
print(o,p)