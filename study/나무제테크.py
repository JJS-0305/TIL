def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

N, M, K = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]
map_list = [[5 for _ in range(N)] for _ in range(N)]    # 양분이 저장된 리스트
tree = [[[] for _ in range(N)] for _ in range(N)]       # 나무의 나이가 저장된 리스트
for i in range(M):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)

cnt = M
while K != 0:
    # 봄, 여름
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                plus = 0    # 여름에 추가할 양분의 양
                for i in range(len(tree[r][c]),0,-1):
                    if map_list[r][c] < tree[r][c][i-1]:
                        plus += tree[r][c][i-1]//2
                        tree[r][c][i-1] = 0
                        cnt -= 1
                    elif tree[r][c][i-1] != 0:
                        map_list[r][c] -= tree[r][c][i-1]
                        tree[r][c][i-1] += 1
                map_list[r][c] += plus
                for j in range(len(tree[r][c])):
                    if tree[r][c][j] != 0:
                        tree[r][c] = tree[r][c][j::]
                        break

    # 가을
    drow = [-1,-1,-1,0,0,1,1,1]
    dcol = [-1,0,1,-1,1,-1,0,1]
    for r in range(N):
        for c in range(N):
            for i in range(len(tree[r][c])):
                if tree[r][c][i] % 5 == 0 and tree[r][c][i] != 0:
                    for j in range(8):
                        test_r = r + drow[j]
                        test_c = c + dcol[j]
                        if iswall(test_r,test_c):
                            tree[test_r][test_c].append(1)
                            cnt += 1
            # 겨울
            map_list[r][c] += A[r][c]


    K -= 1

print(cnt)