A = int(input())
B = int(input())
n3=A*(B%10)
n4=A*(B%100//10)
n5=A*(B//100)
print(n3,n4,n5,A*B,sep='\n')