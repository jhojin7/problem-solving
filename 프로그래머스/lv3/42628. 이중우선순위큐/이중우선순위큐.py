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
            return [0,0]
        # print max, min
        return [self.Q[0], self.Q[-1]]
        

#####

def solution(operations):
    dpq = DoublePQueue()
    for i,op in enumerate(operations):
        op,n = op.split()
        n = int(n)
        print(op,n)
        if op == 'I':
            dpq.insert(n)
        elif op == 'D':
            dpq.delete(n)
    return dpq.fin()