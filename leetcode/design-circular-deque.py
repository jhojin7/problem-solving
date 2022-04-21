'''
'''

class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [None] * k
        self.k = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        self.front = (self.k - self.front-1)%self.k
        if self.deque[self.front] == None:
            self.deque[self.front] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.deque[self.rear] == None:
            self.deque[self.rear] = value
            self.rear = (self.rear+1)%self.k
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque[self.front] != None:
            self.deque[self.front] = None
            self.front = (self.front+1)%self.k
            return True
        else:
            return False
        
    def deleteLast(self) -> bool:
        print(self.front, self.rear)
        if self.deque[self.rear-1] != None:
            self.deque[self.rear-1] = None
            self.rear = (self.rear -1)%self.k
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[self.front]
        
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[self.rear-1]

    def isEmpty(self) -> bool:
        # return self.front == self.rear and self.deque[self.front] == None
        return self.front == (self.rear+1)%self.k and self.deque[self.front] == None
        
    def isFull(self) -> bool:
        return self.front == (self.rear+1)%self.k and self.deque[self.front] != None

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
calls = [
    obj.insertLast(1),
    obj.insertLast(2),
    obj.deleteLast(),
    obj.deleteLast(),
    obj.isEmpty()




    # obj.insertLast(1),
    # obj.insertLast(2),
    # obj.insertFront(3),
    # obj.insertFront(4),
    # obj.getRear(),
    # obj.isFull(),
    # obj.deleteLast(),
    # obj.insertFront(4),
    # obj.getFront()
]
print(obj.deque)
print(calls)
