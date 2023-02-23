import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

def check(board):
    for row in board:
        if row.count('O')==4:
            return 'O'
        if row.count('X')==4:
            return 'X'
        if row.count('X')==3 and row.count('T')==1:
            return 'X'
        if row.count('O')==3 and row.count('T')==1:
            return 'O'
    for j in range(4):
        col = [board[i][j] for i in range(4)]
        if col.count('O')==4:
            return 'O'
        if col.count('X')==4:
            return 'X'
        if col.count('X')==3 and col.count('T')==1:
            return 'X'
        if col.count('O')==3 and col.count('T')==1:
            return 'O'
    diag1 = [board[i][i] for i in range(4)]
    diag2 = [board[i][3-i] for i in range(4)]
    for col in [diag1,diag2]:
        if col.count('O')==4:
            return 'O'
        if col.count('X')==4:
            return 'X'
        if col.count('X')==3 and col.count('T')==1:
            return 'X'
        if col.count('O')==3 and col.count('T')==1:
            return 'O'
    return None

def is_full(board):
    for row in board:
        if '.' in row:
            return False
    return True

def solve(i):
    i+=1
    board = [list(inputchars()) for _ in range(4)]
    # print(board)
    winner = check(board)
    if not is_full(board):
        if winner==None:
            print(f"Case #{i}: Game has not completed")
            return
    if winner=='X':
        print(f"Case #{i}: X won")
        return
    if winner=='O':
        print(f"Case #{i}: O won")
        return
    if winner==None:
        print(f"Case #{i}: Draw")
        return
    # print(f"Case #{i}: ")

for i in range(int(input())):
    solve(i)
    input()