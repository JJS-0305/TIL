def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= M:
        return False
    return True
def bfs(row,col):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[row][col] = 1
    queue = []
    queue.append([row,col])
    # print(queue[0])
    while queue:
        if queue[0] == [N-1,M-1]:
            return visited[N-1][M-1]
        for i in range(4):
            test_r = queue[0][0] + dr[i]
            test_c = queue[0][1] + dc[i]

            if iswall(test_r,test_c):
                # print(test_r,test_c)
                if visited[test_r][test_c] == 0 and data[test_r][test_c] == 1:
                    visited[test_r][test_c] = visited[queue[0][0]][queue[0][1]] + 1
                    queue.append([test_r,test_c])
        queue.pop(0)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
data = [list(map(int,input())) for _ in range(N)]

print(bfs(0,0))