arr = []
s=0
try:
    while 1:
        l = input()
        if l=='':
            arr.append(s)
            s=0
        else:
            s+=int(l)
except: pass
print(sum(sorted(arr,reverse=True)[:3]))
