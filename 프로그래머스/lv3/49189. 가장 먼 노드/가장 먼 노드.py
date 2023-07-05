import collections, heapq, math

def solution(n, edge):
    graph = collections.defaultdict(list)
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    def dijkstra(graph, src):
        dist = [math.inf for _ in range(n+1)]
        dist[src] = 0
        pq = [(0,src)]
        while pq:
            d,x = heapq.heappop(pq)
            if d > dist[x]:
                continue
            for nx in graph[x]:
                if d+1 < dist[nx]:
                    dist[nx] = min(dist[nx],d+1)
                    heapq.heappush(pq,(d+1, nx))
        return dist
    distans = dijkstra(graph, 1)
    maxdist = sorted(distans)[-2]
    return (distans.count(maxdist))
    
                    
                    
                    
            
