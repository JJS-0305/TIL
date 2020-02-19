def bfs(man1, man2):
    que = []
    que.append(man2)
    visited_bfs[man2] = 1
    while True:
        # print(visited_bfs)
        if visited_bfs[man1] != 0:
            return visited_bfs[man1] - 1
        for c in range(1,N+1):
            if relation[que[0]][c] == 1 and visited_bfs[c] == 0:
                visited_bfs[c] = visited_bfs[que[0]] + 1
                que.append(c)
                # print(que)
                # print()
        que.pop(0)

N, M = map(int, input().split())
relation = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    man1, man2 = map(int, input().split())
    relation[man1][man2] = 1
    relation[man2][man1] = 1
# for j in range(N+1):
#     print(relation[j])
# print()
mn = N**2
ans = 0
for r in range(1,N+1):
    tot = 0
    visited = [0] * (N+1)
    visited[r] = 1
    for c in range(1,N+1):
        if relation[r][c] == 1 and visited[c] == 0:
            visited[c] = 1
            tot += 1
        elif visited[c] == 0:
            visited_bfs = [0] * (N + 1)
            tot += bfs(r,c)
            # print(r, c, bfs(r,c))
    # print(r, tot)
    # print()
    if tot < mn:
        mn = tot
        ans = r
print(ans)