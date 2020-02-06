def iswall(r,c):
    if r < 0 or r >= 100:
        return False
    if c < 0 or c >= 100:
        return False
    return True

def route(r,c):
    ladder[r][c] = -1
    # print(r,c)
    col = 0
    if r == 0:
        col += c
    for j in range(3):
        test_r = r + dr[j]
        test_c = c + dc[j]
        if iswall(test_r, test_c):
            # print(test_r, test_c)
            if ladder[test_r][test_c] == 1:
                return route(test_r,test_c)
    return col

dr = [0, 0, -1]
dc = [1, -1, 0]

import sys
sys.stdin = open("ladder_input")

T = 10

for tc in range(T):
    casenum = int(input())
    ladder = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        ladder[i] = list(map(int,input().split()))

    for c in range(100):
        if ladder[99][c] == 2:
            print("#{} {}".format(casenum,route(99,c)))