def find(row, col):
    r = 1
    c = 1

    test_r = row + 1
    test_c = col + 1
    while True:
        if 0 <= test_r < N:
            if ls[test_r][col] != 0:
                test_r += 1
                r+= 1
            else:
                break
        else:
            break
    while True:
        if 0 <= test_c < N:
            if ls[row][test_c] != 0:
                test_c += 1
                c += 1
            else:
                break
        else:
            break
    for i in range(row, row+r):
        for j in range(col, col+c):
            visited[i][j] = 1

    return [r*c,r,c]

T = int(input())

for tc in range(T):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    for row in range(N):
        for col in range(N):
            if ls[row][col] != 0 and visited[row][col] == 0:
                result.append(find(row,col))

    result.sort()
    print("#{} {}".format(tc+1, len(result)), end=" ")
    for i in range(len(result)):
        print(result[i][1], end=" ")
        print(result[i][2], end=" ")
    print()
