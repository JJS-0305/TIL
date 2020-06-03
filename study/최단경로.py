import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    dist = [float('inf')] * (V+1)
    dist[K] = 0
    pq = []
    heapq.heappush(pq,(0, K))

    while pq:
        w, u = heapq.heappop(pq)
        for cost, v in edges[u]:
            via = cost + dist[u]
            if via < dist[v]:
                dist[v] = via
                heapq.heappush(pq,(via, v))

    return dist[1:]

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w,v))

ans = dijkstra()
for i in ans:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

