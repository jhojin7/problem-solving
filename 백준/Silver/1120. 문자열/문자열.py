import math
A,B=input().split()
# print(A,B)
mincnt=math.inf
for i in range(len(B)-len(A)+1):
    BB = B[i:i+len(A)]
    cnt=0
    for j in range(len(BB)):
        if A[j]!=BB[j]: cnt+=1
    # print(A,BB,cnt)
    mincnt=min(mincnt,cnt)
print(mincnt)