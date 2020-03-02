def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True
def dfs(row, col):
    visited[row][col] = 1
    for i in range(4):
        test_r = row + dr[i]
        test_c = col + dc[i]

        if iswall(test_r,test_c):
            # 상하좌우에 내 방보다 1 적은 숫자가 있으면 탈출
            if square[test_r][test_c] == square[row][col] - 1:
                if visited[test_r][test_c] == 0:
                    visited[row][col] = 0
                    return 0
            if square[test_r][test_c] == square[row][col] + 1:
                if visited[test_r][test_c] != 0:
                    visited[row][col] += visited[test_r][test_c]
                    break
                else:
                    visited[row][col] += dfs(test_r,test_c)
                    break
    return visited[row][col]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    my_max = 0
    ans = N**2
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                cnt = dfs(r,c)

                if cnt > my_max:
                    my_max = cnt
                    ans = square[r][c]
                elif cnt == my_max:
                    if square[r][c] < ans:
                        ans = square[r][c]

    print("#{} {} {}".format(tc,ans,my_max))