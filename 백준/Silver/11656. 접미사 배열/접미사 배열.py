str = input().strip();arr = []
for i in range(len(str)):arr.append(str[i:])
print(*sorted(arr),sep='\n')