s=input().strip()
aaa = "aeiou"
cnt = 0
for c in s:
    if c in aaa:
        cnt +=1
print(cnt)