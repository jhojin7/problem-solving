fx = input().strip()
if fx=='0': 
    print("W")
    exit()
f = fx.split('x')
if 'x' not in fx:
    f = ['',fx]
# print(f)
if f==['','0']:
    print(0)
    exit()
elif f==['','']:
    f = ['1','0']

a,b=0,0
ans = ""
if f[0]=='':
    if f[1]=='': pass
    elif f[1]=='1': 
        ans+=f"x+W"
    elif f[1]=='+1': 
        ans+=f"x+W"
    elif f[1]=='-1':
        ans+=f"-x+W"
    elif int(f[1])>0:
        ans+=f"{int(f[1])}x+W"
    elif int(f[1])<0:
        ans+=f"{int(f[1])}x+W"

else:# elif int(f[0])!=1:
    a = int(f[0])
    if a==1:
        ans+="xx+W"
    elif a//2==1:
        ans+="xx"
    elif a//2==-1:
        ans+="-xx"
    else:
        ans+=f"{a//2}xx"
    if f[1]=='': 
        ans+="+W"
    elif f[1]=='+1': 
        ans+=f"+x+W"
    elif f[1]=='-1':
        ans+=f"-x+W"
    elif int(f[1])>0:
        ans+=f"+{int(f[1])}x+W"
    elif int(f[1])<0:
        ans+=f"{int(f[1])}x+W"
    # else:
    #     ans+="+W"
print(ans)