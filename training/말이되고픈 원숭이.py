from collections import deque

def iswall(r,c):
    if r < 0 or r >= H:
        return False
    if c < 0 or c >= W:
        return False
    return True
def bfs(row,col,k):
    que = deque()
    que.append((row,col,k))
    while que:
        r,c,k = que.popleft()
        if r == H-1 and c == W-1:
            return visited[k][r][c]
        for i in range(12):
            if i >= 4 and k+1 > K:
                break
            test_r = r + drow[i]
            test_c = c + dcol[i]
            # if test_r == H-1 and test_c == W-1:
            #     return visited[k][r][c] + 1
            if iswall(test_r,test_c) and map_list[test_r][test_c] != 1:
                if i < 4:
                    if visited[k][test_r][test_c] == 0:
                        visited[k][test_r][test_c] = visited[k][r][c] + 1
                        que.append((test_r,test_c,k))
                else:
                    if visited[k+1][test_r][test_c] == 0:
                        visited[k+1][test_r][test_c] = visited[k][r][c] + 1
                        que.append((test_r,test_c,k+1))
    return -1

drow = [1,-1,0,0,2,2,-2,-2,1,1,-1,-1]
dcol = [0,0,1,-1,1,-1,1,-1,2,-2,2,-2]

K = int(input())
W, H = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(H)]

visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

ans = bfs(0,0,0)
print(ans)
