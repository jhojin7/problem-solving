s=0
for _ in range(5):
    x=int(input())
    if x<40: s+=40
    else: s+=x
print(s//5)