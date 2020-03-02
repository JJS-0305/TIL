def my_type(s):
    if s == 1:
        return [0, 1, 2, 3]
    elif s == 2:
        return [0, 1]
    elif s == 3:
        return [2, 3]
    elif s == 4:
        return [0, 3]
    elif s == 5:
        return [1, 3]
    elif s == 6:
        return [1, 2]
    elif s == 7:
        return [0, 2]

def bfs(row, col, L):
    if L == 1:
        return 1

    visited[row][col] = 1
    queue = []
    queue.append(row)
    queue.append(col)

    cnt = 1
    while queue:
        row1 = queue.pop(0)
        col1 = queue.pop(0)
        for i in my_type(Map[row1][col1]):
            test_r = row1 + dr[i]
            test_c = col1 + dc[i]

            if 0 <= test_r < N and 0 <= test_c < M:
                if visited[test_r][test_c] == 0:
                    if i == 0:
                        if Map[test_r][test_c] == 1 or Map[test_r][test_c] == 2 or Map[test_r][test_c] == 5 or Map[test_r][test_c] == 6:
                            cnt += 1
                            visited[test_r][test_c] = visited[row1][col1] + 1
                            if visited[test_r][test_c] < L:
                                queue.append(test_r)
                                queue.append(test_c)
                    elif i == 1:
                        if Map[test_r][test_c] == 1 or Map[test_r][test_c] == 2 or Map[test_r][test_c] == 4 or Map[test_r][test_c] == 7:
                            cnt += 1
                            visited[test_r][test_c] = visited[row1][col1] + 1
                            if visited[test_r][test_c] < L:
                                queue.append(test_r)
                                queue.append(test_c)
                    elif i == 2:
                        if Map[test_r][test_c] == 1 or Map[test_r][test_c] == 3 or Map[test_r][test_c] == 4 or Map[test_r][test_c] == 5:
                            cnt += 1
                            visited[test_r][test_c] = visited[row1][col1] + 1
                            if visited[test_r][test_c] < L:
                                queue.append(test_r)
                                queue.append(test_c)
                    elif i == 3:
                        if Map[test_r][test_c] == 1 or Map[test_r][test_c] == 3 or Map[test_r][test_c] == 6 or Map[test_r][test_c] == 7:
                            cnt += 1
                            visited[test_r][test_c] = visited[row1][col1] + 1
                            if visited[test_r][test_c] < L:
                                queue.append(test_r)
                                queue.append(test_c)

    return cnt

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    print("#{} {}".format(tc, bfs(R,C,L)))