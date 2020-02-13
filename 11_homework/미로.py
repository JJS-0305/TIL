import sys
sys.stdin = open("미로_input.txt")

def chk(row,col):
    # print(row,col)
    global result

    if miro[row][col] != 3:
        miro[row][col] = -1
    for i in range(4):
        test_r = row + dr[i]
        test_c = col + dc[i]

        if miro[test_r][test_c] == 0:
            chk(test_r, test_c)
        elif miro[test_r][test_c] == 3:
            result = 1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = 10
for tc in range(T):
    casenum = int(input())
    miro = [list(map(int,input())) for _ in range(16)]
    result = 0
    chk(1,1)
    print("#{} {}".format(casenum, result))