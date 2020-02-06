import sys
sys.stdin = open("input")

def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def chk(row, col, clr, dr, dc):
    cnt = 0
    while (iswall(row,col) and pan[row][col] != 0):
        if pan[row][col] == clr:
            cnt += 1
            break
        else:
            row += dr
            col += dc
    return cnt

def change(row, col, clr):
    for j in range(8):
        test_r = row + dr[j]
        test_c = col + dc[j]

        result = 0
        if iswall(row, col):
            result = chk(test_r,test_c,clr,dr[j],dc[j])
            # print(result)

        if result == 1:
            while(iswall(row,col) and pan[test_r][test_c] != clr):
                pan[test_r][test_c] = clr
                test_r += dr[j]
                test_c += dc[j]

dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1 ,1, -1]

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pan = [[0 for _ in range(N)] for _ in range(N)]
    n = int(N//2) -1
    # print(n)
    pan[n][n] = 2
    pan[n][n+1] = 1
    pan[n+1][n] = 1
    pan[n+1][n+1] = 2
    # print(pan)
    # col = [0] * M
    # row = [0] * M
    # clr = [0] * M
    for i in range(M):
        col, row, clr = map(int, input().split())
        pan[row-1][col-1] = clr
        change(row-1,col-1,clr)

    ans_1 = 0
    ans_2 = 0
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 1:
                ans_1 += 1
            elif pan[i][j] == 2:
                ans_2 += 1
    print("#{} {} {}".format(tc+1, ans_1, ans_2))
        # print(pan[0])
        # print(pan[1])
        # print(pan[2])
        # print(pan[3])
        # print()