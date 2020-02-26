def bfs(man1, man2, cnt):
    if relation[man2][man1] == 1:
        return
    for c in range(N+1):
        if relation[man2][c] == 1 and visited_bfs[c] == 0:
            visited_bfs[c] = 1
            cnt += bfs(man1,c,cnt)
    return cnt

N, M = map(int, input().split())

relation = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    man1, man2 = map(int, input().split())
    relation[man1][man2] = 1
    relation[man2][man1] = 1

for j in range(N+1):
    print(relation[j])
mn = N**2
ans = 0
for r in range(1,N+1):
    tot = 0
    visited = [0] * (N+1)
    visited[r] = 1
    visited_bfs = [0] * (N+1)
    for c in range(1,N+1):
        if relation[r][c] == 1 and visited[c] == 0:
            visited[c] = 1
            tot += 1
        else:
           tot += bfs(r,c,0)
           print(bfs(r,c,0))

    print(r, tot)
    if tot < mn:
        mn = tot
        ans = r
print(ans)