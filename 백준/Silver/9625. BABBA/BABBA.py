k=int(input())
A=[0 for _ in range(60)]
B=[0 for _ in range(60)]
A[0]=0
B[0]=1
for i in range(1,k):
    A[i]=B[i-1]
    B[i]=B[i-1]+A[i-1]
print(A[k-1],B[k-1])