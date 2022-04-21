'''
https://leetcode.com/submissions/detail/676361457/
LATE
'''
import collections

class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * k
        self.k = k
        self.head = 0
        self.tail = 0
        print(self.cq, self.k)

    def enQueue(self, value: int) -> bool:
        if self.cq[self.tail] == None:
            self.cq[self.tail] = value
            self.tail = (self.tail+1) % self.k
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.cq[self.head] != None:
            self.cq[self.head] = None
            self.head = (self.head+1) % self.k
            return True
        else:
            return False
        
    def Front(self) -> int:
        if self.cq[self.head] == None:
            return -1
        else:
            return self.cq[self.head]

    def Rear(self) -> int:
        if self.cq[self.tail-1] == None:
            return -1
        else:
            return self.cq[self.tail-1]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.cq[self.head] == None

    def isFull(self) -> bool:
        return self.head == self.tail and self.cq[self.head] != None
        


# Your MyCircularQueue object will be instantiated and called as such:
k = 3
obj = MyCircularQueue(k)
calls = [
    obj.enQueue(1),
    obj.enQueue(2),
    obj.enQueue(3),
    obj.enQueue(4),
    obj.Rear(),
    obj.isFull(),
    obj.deQueue(),
    obj.enQueue(4),
    obj.Front()
]
print(calls)
