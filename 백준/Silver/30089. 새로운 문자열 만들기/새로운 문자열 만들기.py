for _ in range(int(input())):
    s = input()
    arr = []
    for i in range(len(s)):
        for j in range(len(s)):
            ss = s[:i]+s[j::-1]
            # print(ss)
            if ss == ss[::-1] and ss.find(s) != -1:
                arr.append(ss)
    arr.sort(key=lambda x: len(x))
    print(arr[0])