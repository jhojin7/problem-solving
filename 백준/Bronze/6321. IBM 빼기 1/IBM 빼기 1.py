for i in range(int(input())):
    st = list(input().strip())
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = []
    for c in st:
        x = caps[(caps.index(c)+1)%26]
        ans.append(x)
    print(f"String #{i+1}")
    print("".join(ans))
    print()