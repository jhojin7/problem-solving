C = int(input())
for _ in range(C):
    N,*arr = map(int,input().split())
    # print(N,arr,sum(arr)/N)
    avg = sum(arr)/N
    above_avg = [a for a in arr if a>avg]
    ans = len(above_avg)/N
    print("{:2.3%}".format(ans))