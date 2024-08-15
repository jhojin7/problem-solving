word = input()
w,h = 1+4*len(word), 5
arr = [['.' for _ in range(w)] for _ in range(h)]

def do(x,y, ch):
    arr[0][y] = ch
    for ii in range(3):
        arr[ii][y-ii] = ch
        arr[ii][y+ii] = ch
    arr[3][y+1] = ch
    arr[3][y-1] = ch
    arr[4][y] = ch

for i in range(len(word)):
    x,y = 2,2+(4*i)
    arr[x][y] = word[i]
    if (i+1)%3==0:
        # do(x,y,'*')
        continue
    else:
        do(x,y,'#')

for i in range(len(word)):
    x,y = 2,2+(4*i)
    arr[x][y] = word[i]
    if (i+1)%3==0:
        do(x,y,'*')
    else:
        # do(x,y,'#')
        continue

print(*[''.join(row) for row in arr], sep='\n')