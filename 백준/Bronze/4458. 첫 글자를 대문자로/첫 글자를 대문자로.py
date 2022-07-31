n = int(input())
for _ in range(n):
    line = list(input().split()) 
    for i,w in enumerate(line):
        if i==0:
            print(w[0].capitalize(),end='')
            print(w[1:],end=' ')
        else: print(w,end=' ')
    print()