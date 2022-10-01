N,M=map(int,input().split())
A,B=[],[]
for _ in range(M):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
minA = min(A)
minB = min(B)

# 묶음+낱개로
aa=minA*(N//6)
aa+=minB*(N%6)
# 묶음으로
cc=minA*(N//6)
cc+= minA*(0 if N%6==0 else 1)
# 낱개로
bb=minB*(N)
# print(aa,bb,cc)
print(min(aa,bb,cc))