import sys
sys.stdin = open('최소합_input.txt')

def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def min_num(row,col):
    global tot
    global ans
    if row == N-1 and col == N-1:
        if tot < ans:
            ans = tot
        return

    test_r = row + 1
    test_c = col + 1

    if iswall(test_r,col):
        tot += num[test_r][col]
        min_num(test_r,col)
        tot -= num[test_r][col]
    if iswall(row,test_c):
        tot += num[row][test_c]
        min_num(row,test_c)
        tot -= num[row][test_c]



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    tot = num[0][0]
    ans = 987654321
    min_num(0,0)
    print("#{} {}".format(tc,ans))