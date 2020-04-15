from collections import deque

def bfs(F,S,G,U,D):
    visited = [0] * (F + 1)
    queue = deque()
    visited[S] = 1
    queue.append(S)
    while queue:
        S = queue.popleft()
        if S == G:
            return visited[S] - 1
        if S+U <= F and visited[S+U] == 0:
            visited[S+U] = visited[S] + 1
            queue.append(S+U)
        if S-D >= 1 and visited[S-D] == 0:
            visited[S-D] = visited[S] + 1
            queue.append(S-D)
    return "use the stairs"

F, S, G, U, D = map(int, input().split())

ans = bfs(F,S,G,U,D)
print(ans)