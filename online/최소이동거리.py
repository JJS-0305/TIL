import heapq
import sys
sys.stdin = open('최소이동거리_input.txt')

def dijkstar():
    dist = [float('inf')] * (V + 1)
    dist[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        cost, st = heapq.heappop(pq)

        for ed, w in adj[st]:
            via = w + dist[st]
            if dist[ed] > via:
                dist[ed] = via
                heapq.heappush(pq, (via, ed))

    return dist[-1]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int,input().split())
        adj[s].append((e, w))

    print("#{} {}".format(tc,dijkstar()))


# 3
# 2 3
# 0 1 1
# 0 2 6
# 1 2 1
# 4 7
# 0 1 9
# 0 2 3
# 0 3 7
# 1 4 2
# 2 3 8
# 2 4 1
# 3 4 8
# 4 6
# 0 1 10
# 0 2 7
# 1 4 2
# 2 3 10
# 2 4 3
# 3 4 10
