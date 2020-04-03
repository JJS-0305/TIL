import sys
sys.stdin = open('미로의거리_input2.txt')

def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def bfs(row,col):
    queue = []
    queue.append(row)
    queue.append(col)
    miro[row][col] = -1
    while queue:
        r = queue.pop(0)
        c = queue.pop(0)

        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]

            if iswall(test_r,test_c):
                if miro[test_r][test_c] == 0:
                    queue.append(test_r)
                    queue.append(test_c)
                    miro[test_r][test_c] = miro[r][c] - 1
                elif miro[test_r][test_c] == 3:
                    return -(miro[r][c] + 1)
    return 0


drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

T = int(input())

for tc in range(T):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if miro[row][col] == 2:
                print("#{} {}".format(tc+1,bfs(row,col)))
                break
