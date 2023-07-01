i=0
for _ in range(10):
    i+=int(input())
print("NESW"[i%4])