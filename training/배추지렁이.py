import sys
sys.stdin = open("test_input")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def iswall(x,y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def chk(x,y):
    ls[x][y] = 0

    for a in range(4):
        test_x = x + dx[a]
        test_y = y + dy[a]

        if iswall(test_x,test_y):
            if ls[test_x][test_y] == 1:
                chk(test_x, test_y)

T = int(input())

for tc in range(T):
    M, N, K = map(int,input().split())
    ls = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    for _ in range(K):
        col, row = map(int, input().split())
        ls[row][col] = 1

    # print(ls)
    for r in range(N):
        for c in range(M):
            if ls[r][c] == 1:
                chk(r, c)
                result += 1
                # print(ls)
                # print(result)

    print(result)