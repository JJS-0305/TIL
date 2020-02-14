def ripe(row,col):
    for i in range(4):
        test_r = row + dr[i]
        test_c = col + dc[i]

        if 0 <= test_r < N and 0 <= test_c < M:
            if tomato[test_r][test_c] == 0:
                tomato[test_r][test_c] = 1

def fail_chk(row, col):
    chk = 0
    for i in range(4):
        test_r = row + dr[i]
        test_c = col + dc[i]

        if test_r < 0 or test_r >= N or test_c < 0 or test_c >= M:
            chk += 1
        elif tomato[test_r][test_c] == -1:
            chk += 1
    if chk == 4:
        return False

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

M, N = map(int, input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]
stack = []
cnt = 0
while True:
    chk = 0
    day_zero = 0
    for row in range(N):
        for col in range(M):
            if tomato[row][col] == 0:
                day_zero += 1
                if fail_chk(row,col) == False:
                    chk += 1
                    break
                break

    if day_zero == 0:
        break

    if chk > 0 :
        cnt = -1
        break

    for r in range(N):
        for c in range(M):
            if tomato[r][c] == 1:
                stack.append(r)
                stack.append(c)

    else:
        while True:
            col = stack.pop()
            row = stack.pop()
            ripe(row,col)

            if len(stack) == 0:
                cnt += 1
                break

print(cnt)