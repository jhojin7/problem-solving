import heapq

maxheap = []
def delete_max():
    pass
def delete_max():
    pass

def solution(operations):
    for op in operations:
        cmd,x = op.split()
        x = int(x)
        print(cmd,x)
        print(maxheap)
        if cmd == 'I':
            heapq.heappush(maxheap,-x)
        elif cmd == 'D':
            if x == 1:
                delete_max()
            elif x == -1:
                delete_min()
    print(maxheap)
    return [0,0]