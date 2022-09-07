n=int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

ans = 0
# i = 0
# while i<len(dist):
#     curdist = dist[i]
#     curprice = price[i]
#     while (i+1<len(price) and i+1<len(dist) 
#         and price[i] < price[i+1]):
#         curdist += dist[i+1]
#         i+=1
#     ans += curdist*curprice
#     i+=1
m = price[0]
for i in range(len(dist)):
    if price[i]<m:
        m=price[i]
    ans+=m*dist[i]
print(ans)