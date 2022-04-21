'''
https://leetcode.com/submissions/detail/676080756/
02:46 left
https://leetcode.com/submissions/detail/676100724/
'''
import collections
"""
class MyStack:
    def __init__(self):
        # only use queue methods
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        print(f"push {x}")

    def pop(self) -> int:
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        while len(self.queue2) != 1:
            self.queue1.append(self.queue2.popleft())
        popped = self.queue2.popleft()
        print(f"pop {popped}")
        return popped

    def top(self) -> int:
        popped = self.pop()
        self.push(popped)
        print(f"top {popped}")
        return popped

    def empty(self) -> bool:
        return len(self.queue1)==0 and len(self.queue2)==0
"""

class MyStack:
    def __init__(self) -> None:
        self.q = collections.deque()

    def push(self,x:int)->None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) ->bool:
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
calls = [
    obj.push(1),
    obj.push(2),
    obj.push(3),
    obj.push(4),
    obj.push(5),
    obj.top(),
    obj.pop(),
    obj.pop(),
    obj.pop(),
    obj.pop(),
    obj.pop(),
    obj.empty()
]
print(calls)