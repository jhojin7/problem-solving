line = ""
for i in range(14,len(line)):
    window = line[i-14:i]
    print(i,window,set(window.strip()))
    if len(window)==len(set(window.strip())):
        print(i,window,set(window.strip()))
        break
