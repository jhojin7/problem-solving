import heapq
def solution(arr, K):
    heapq.heapify(arr)
    i = 0
    while len(arr)>=2 and arr[0]<K:
        i+=1
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        new = a+b*2
        heapq.heappush(arr, new)
    if arr[0]<K:
        return -1
    return i

