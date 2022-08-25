N=int(input())
origin = N
cnt = 0
while 1:
    cnt+=1
    a,b=N//10,N%10
    nn=(b*10)+((a+b)%10)
    if nn==origin: break
    N = nn
print(cnt)