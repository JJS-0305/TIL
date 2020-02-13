def iswall(r,c):
    if r < 0 or r >= 100:
        return False
    if c < 0 or c >= 100:
        return False
    return True

def short_chk(row,col,cnt):
    visited[row][col] = 1
    if row == 99:
        return cnt
    for i in range(3):
        test_r = row + dr[i]
        test_c = col + dc[i]

        if iswall(test_r,test_c):
            if ladder[test_r][test_c] == 1 and visited[test_r][test_c] == 0:
                return short_chk(test_r,test_c,cnt+1)
dr = [0, 0, 1]
dc = [1, -1, 0]

import sys
sys.stdin = open("ladder2_input")

T = 10

for tc in range(T):
    casenum = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    mn = 987654321
    ans = 0
    cnt = 0
    for c in range(100):
        if ladder[0][c] == 1:
            visited = [[0 for _ in range(100)] for _ in range(100)]
            cnt = short_chk(0,c,0)
            if cnt < mn:
                mn = cnt
                ans = c
    print("#{} {}".format(casenum, ans))