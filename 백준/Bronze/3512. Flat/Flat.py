import sys,collections
input = sys.stdin.readline
n,c = map(int,input().split())
rooms = collections.defaultdict(int)
for _ in range(n):
    ai,ti =input().split()
    rooms[ti] += int(ai)
# print(rooms)

s = sum(rooms.values())
print(s)
print(rooms["bedroom"])

price=((s-rooms["balcony"]/2)*c)
if price%1==0:print(int(price))
else:print(price)