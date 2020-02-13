import sys
sys.stdin = open("test3_input.txt")

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in range(V+1):
        if G[v][i] == 1 and visited[i] == 0:
            dfs(i)

V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]

# 인접행렬로 저장
for i in range(0, len(temp), 2):
    row = temp[i]
    col = temp[i+1]
    G[row][col] += 1
    G[col][row] += 1


# 입력확인
for i in range(V+1):
    print("{} {}".format(i, G[i]))

dfs(1)