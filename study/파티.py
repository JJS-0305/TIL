import heapq

def dijkstra(V):
    dist = [float('inf')] * (N+1)
    dist[V] = 0
    pq = []
    heapq.heappush(pq,(0,V))
    while pq:
        cost, ed = heapq.heappop(pq)
        for w, next in adj[ed]:
            via = dist[ed] + w
            if dist[next] > via:
                dist[next] = via
                heapq.heappush(pq, (via, next))
    return dist

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    st, ed, T = map(int, input().split())
    adj[st].append((T,ed))

mx = 0
ls = dijkstra(X)
for i in range(1,N+1):
    d = dijkstra(i)[X] + ls[i]
    if d > mx:
        mx = d
print(mx)