s=input().strip()
caps="ABCDEFGHIJKLNMOPQRSTUVWXYZ"

has_caps=has_underscore=False
for c in s:
    if c in caps:
        has_caps=True
    if c=='_':
        has_underscore=True

if has_caps and has_underscore:
    print("Error!")
elif has_underscore:
    if s[0]=='_':
        print("Error!")
        exit()
    try:
        t = s.split('_')
        ans=[t[0]]
        for str in t[1:]:
            ans.append(str[0].capitalize()+str[1:])
        print("".join(ans))
    except:
        print("Error!")
        exit()
elif has_caps:
    if s[0] in caps:
        print("Error!")
        exit()
    try:
        idxes = [0]+[i for i in range(1,len(s)) if s[i] in caps]+[len(s)]
        ans=[]
        # print(s,idxes)
        for i in range(len(idxes)-1):
            # print(s[idxes[i]:idxes[i+1]])
            ans.append(s[idxes[i]:idxes[i+1]].lower())
        # print(ans)
    except:
        print("Error!")
        exit()
    print("_".join(ans))
else:
    print(s)