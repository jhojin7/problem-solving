s=input()
chars=[]
uu=[]
for i in range(len(s)):
    if s[i]=='U':
        chars.append((i,s[i]))
        uu.append(i)
    elif s[i]=='C': chars.append((i,s[i]))
    elif s[i]=='P': chars.append((i,s[i]))
# print(chars)

if len(chars)<4:
    print("I hate UCPC")
    exit()

# cnt=0
for i in uu:
    ans=[s[i]]
    for j,ch in chars:
        if j<=i: continue
        # print(j,ch)
        if ans[-1]=='U' and ch=='C':
            ans.append(ch)
        elif ans[-1]=='C' and ch=='P':
            ans.append(ch)
        elif ans[-1]=='P' and ch=='C':
            ans.append(ch)
            print("I love UCPC")
            exit()

print("I hate UCPC")