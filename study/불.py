from collections import deque

def iswall(row,col):
    if row < 0 or row >= h:
        return False
    if col < 0 or col >= w:
        return False
    return True

def bfs():
    queue = deque()
    for r in range(h):
        for c in range(w):
            if map_list[r][c] == '*':
                queue.append((r,c))

    while queue:
        r , c = queue.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r,test_c):
                if visited[test_r][test_c] == 0 and (map_list[test_r][test_c] == '.' or map_list[test_r][test_c] == '@'):
                    visited[test_r][test_c] = visited[r][c] + 1
                    queue.append((test_r,test_c))

def bfs2(row,col):
    global mn
    queue = deque()
    queue.append((row,col))
    visited[row][col] = 0
    while queue:

        r,c = queue.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r,test_c):
                if (visited[test_r][test_c] == 0 or visited[test_r][test_c] > (visited[r][c] -1) * (-1)) and map_list[test_r][test_c] == '.':
                    visited[test_r][test_c] = visited[r][c] - 1
                    queue.append((test_r, test_c))
            else:
                return (visited[r][c] - 1) * (-1)

    return 'IMPOSSIBLE'

drow = [1,-1,0,0]
dcol = [0,0,1,-1]

T = int(input())

for tc in range(1,T+1):
    w, h = map(int, input().split())
    map_list = [list(input()) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    bfs()
    for i in range(h):
        print(visited[i])
    print()
    for height in range(h):
        for width in range(w):
            if map_list[height][width] == '@':
                ans = bfs2(height,width)

    for i in range(h):
        print(visited[i])
    print()
    print(ans)
