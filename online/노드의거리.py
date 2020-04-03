import sys
sys.stdin=open('노드의거리_input.txt')

def bfs(S, G):
    queue = []
    visited = [0] * (V+1)
    queue.append(S)
    visited[S] = 1
    while queue:
        st = queue.pop(0)
        for i in range(1,V+1):
            if graph[st][i] == 1 and visited[i] == 0:
                if i == G:
                    return visited[st]
                queue.append(i)
                visited[i] = visited[st] + 1
    return 0
T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        s, g = map(int, input().split())
        graph[s][g] = 1
        graph[g][s] = 1
    S, G = map(int, input().split())

    print("#{} {}".format(tc+1, bfs(S,G)))