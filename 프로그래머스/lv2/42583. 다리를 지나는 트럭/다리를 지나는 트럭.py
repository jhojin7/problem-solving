import collections
def solution(bridge_length, weight, truck_weights):
    L,W,trucks = bridge_length, weight, truck_weights
    trucks = collections.deque(trucks)
    bridge = collections.deque([0 for _ in range(L)])
    out = []
    time = 0
    onbridge = 0
    
    while bridge:
        x = bridge.popleft()
        onbridge-=x
        time +=1
        if trucks:
            if trucks[0]+onbridge<=W:
                bridge.append(trucks.popleft())
                onbridge+=bridge[-1]
            else: bridge.append(0)
    print(time)
    return time
