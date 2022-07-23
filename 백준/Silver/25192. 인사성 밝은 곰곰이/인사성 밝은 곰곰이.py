import sys
input = sys.stdin.readline

N = int(input())
users = set()
cnt = 0
for _ in range(N):
    chat = input().strip()
    # print(chat,users)
    if chat == "ENTER":
        users = set()
        continue
    if chat not in users:
        users.add(chat)
        cnt +=1
print(cnt)
