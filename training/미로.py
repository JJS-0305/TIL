def iswall(r,c):
    if r < 0 or r >= N:
        return False
    if c < 0 or c >= N:
        return False
    return True

def escape(row,col):
    result = 0
    if miro[row][col] == 3:
        result += 1
    miro[row][col] = -1
    for j in range(4):
        test_r = row + dr[j]
        test_c = col + dc[j]
        # print(test_r, test_c)

        if iswall(test_r, test_c):
            if miro[test_r][test_c] == 0 or miro[test_r][test_c] == 3:
                result += escape(test_r, test_c)
    return result


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
    N = int(input())
    miro = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        miro[i] = list(map(int, input()))
    # print(miro)


    st_r = 0
    st_c = 0
    # 시작점 찾기
    for r in range(len(miro)):
        for c in range(len(miro[r])):
            if miro[r][c] == 2:
                st_r = r
                st_c = c
    # print(st_r, st_c)
    print("#{} {}".format(tc+1,escape(st_r, st_c)))
