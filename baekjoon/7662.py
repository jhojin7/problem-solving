"""
problem: https://www.acmicpc.net/problem/7662
tle: 
    - https://www.acmicpc.net/submit/7662/44422148
    - https://www.acmicpc.net/source/44421662

"""
import sys
from io import StringIO
testcases = """
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
""".strip()
sys.stdin = StringIO(testcases)

class DoublePQueue:
    def __init__(self) -> None:
        """Q: int list. descending order"""
        self.Q = []

    def insert(self, n:int):
        "I n: insert int n to Q"
        # print("insert",n,self.Q)
        # if queue empty, just insert
        if self.Q == []:
            self.Q.append(n)
            return
        # insert at descending order
        for i in range(len(self.Q)):
            if n > self.Q[i]:
                self.Q.insert(i,n)        
                return
        # if nothing inserted, simply append
        self.Q.append(n)
        return

    def delete(self, _op:int):
        """D n: delete number from Q
        op=1: delete max
        op=-1: delete min"""
        # print("delete",_op,self.Q)
        # if queue empty, pass
        if self.Q == []:
            return
        # delete max
        if _op == 1:
            self.Q.pop(0)
        # delete min
        elif _op == -1:
            self.Q.pop()
    
    def fin(self):
        # if queue empty
        if self.Q == []:
            print("EMPTY")
            return
        # print max, min
        print(self.Q[0], self.Q[-1], sep=" ")

#####
test_cnt = int(input())
for _ in range(test_cnt):
    dpq = DoublePQueue()
    op_cnt = int(input())
    for _ in range(op_cnt):
        x = input().split()
        op,n = str(x[0]),int(x[1])
        if op == 'I':
            dpq.insert(n)
        elif op == 'D':
            dpq.delete(n)
    dpq.fin()