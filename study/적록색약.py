def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def chk_region(row, col, clr):

    for i in range(4):
        test_r = row + drow[i]
        test_c = col + dcol[i]

        if iswall(test_r,test_c) and visited[test_r][test_c] == 0:
            if data[test_r][test_c] == clr:
                visited[test_r][test_c] = 1
                chk_region(test_r,test_c,clr)


drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

N = int(input())
data = [list(map(str, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            cnt += 1
            chk_region(r,c,data[r][c])
cnt2 = 0
visited = [[0 for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if data[r][c] == 'R':
            data[r][c] = 'G'

for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            cnt2 += 1
            chk_region(r,c,data[r][c])

print(cnt, cnt2)