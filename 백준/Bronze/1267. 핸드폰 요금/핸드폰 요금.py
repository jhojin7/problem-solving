N=int(input())
arr = list(map(int,input().split()))
Y, M =0,0
for a in arr:
    Y+=(a//30)*10+10
    M+=(a//60)*15+15
if Y==M:
    print("Y M "+str(Y))
elif Y<M:
    print("Y "+str(Y))
else:
    print("M "+str(M))