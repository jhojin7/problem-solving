N=int(input())
seats=list(input().strip())
ll=seats.count('L')
ss=seats.count('S')
if ll>0: print(ll//2+ss+1)
else: print(ss)