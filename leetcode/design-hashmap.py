'''
https://leetcode.com/submissions/detail/678139383/
'''
class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.map)):
            (k,v) = self.map[i]
            if k==key: 
                self.map[i] = (key,value)
            # if self.map[i][0]== key:
            #     self.map[i][1] = value
        if (key,value) not in self.map:
            self.map.append((key,value))
        

    def get(self, key: int) -> int:
        for (k,v) in self.map:
            if k == key:
                return v 
        return -1

    def remove(self, key: int) -> None:
        for x in self.map:
            (k,v) = x
            if k == key:
                self.map.remove(x)

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
calls = [
    obj.put(1,1),
    obj.put(2,2),
    obj.get(1),
    obj.get(3),
    obj.put(2,1),
    obj.get(2),
    obj.remove(2),
    obj.get(2)
]
print("fin ", obj.map)
print(calls)