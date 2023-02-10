import sys
input = sys.stdin.readline
N = int(input())
meetings = []
for _ in range(N):
    start,fin = map(int,input().split())
    meetings.append((start,fin))
meetings.sort(key=lambda x: (x[1],x[0]))
# print(meetings)

saved = []
for a,b in meetings:
    if not saved:
        saved.append((a,b))
        continue
    prev_a,prev_b = saved[-1]
    if prev_b <= a:
        saved.append((a,b))

# print(*saved,sep='\n')
print(len(saved))