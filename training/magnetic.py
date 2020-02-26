def move(row,col,NS):
    global cnt
    if NS == 1:
        test_row = row + 1
        if test_row < 0 or test_row >= N:
            return
        elif data[test_row][col] == 2:
            visited[test_row] = 1
            cnt += 1
            return
        elif visited[test_row] == 0:
            move(test_row,col,NS)

    elif NS == 2:
        test_row = row - 1
        if test_row < 0 or test_row >= N:
            return
        elif data[test_row][col] == 1:
            visited[test_row] = 1
            cnt += 1
            return
        elif visited[test_row] == 0:
            move(test_row,col,NS)

    return

T = 1
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for row in range(N):
        for col in range(N):
            if data[row][col] != 0:
                # print(data[row][col])
                visited = [0] * N
                move(row,col,data[row][col])
    print(cnt)