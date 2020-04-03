import sys
sys.setrecursionlimit(10**6)
def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def dfs(row, col):
    if dp_list[row][col]:
        return dp_list[row][col]
    dp_list[row][col] = 1
    for i in range(4):
        test_r = row + drow[i]
        test_c = col + dcol[i]
        if iswall(test_r,test_c):
            if map_list[test_r][test_c] > map_list[row][col]:
                dp_list[row][col] = max(dp_list[row][col], dfs(test_r,test_c)+1)
    return dp_list[row][col]

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]
dp_list = [[0 for _ in range(N)] for _ in range(N)]

ans = 0
for r in range(N):
    for c in range(N):
        dp_list[r][c] = dfs(r,c)
        if dp_list[r][c] > ans:
            ans = dp_list[r][c]

print(ans)