import collections

class MyQueue:
    def __init__(self):
        # self.stack = collections.deque()
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # self.stack.append(x)
        self.stack1.append(x)

    def pop(self) -> int:
        # return self.stack.pop()
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        # return self.stack[0]
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] 
        
    def empty(self) -> bool:
        return len(self.stack1)==0 and len(self.stack2)==0
        

obj = MyQueue()
calls = [
    obj.push(1),
    obj.push(2),
    obj.push(3),
    obj.peek(),
    obj.push(4),
    obj.empty(),
    obj.peek(),
    obj.pop(),
    obj.pop(),
    obj.pop(),
    obj.pop(),
    obj.empty()
]
print(calls)


# https://leetcode.com/submissions/detail/676241014/
# 2min left