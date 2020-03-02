T = int(input())

for tc in range(1,T+1):
    H, W = map(int, input().split())
    sand = [list(map(str, input())) for _ in range(H)]

    for r in range(H):
        for c in range(W):
            if sand[r][c] == '.':
                sand[r][c] = 0

    for i in range(H):
        sand[i] = list(map(int, sand[i]))

    dr = [1, -1, 1, -1, 1, -1, 0, 0]
    dc = [0, 0, 1, 1, -1, -1, 1, -1]

    chk = 0
    while True:
        visited = [[0 for _ in range(W)] for _ in range(H)]
        tot = 0
        for row in range(1,H-1):
            for col in range(1,W-1):
                if sand[row][col] != 0 and sand[row][col] != 9 and visited[row][col] == 0:
                    cnt = 0
                    for i in range(8):
                        test_r = row + dr[i]
                        test_c = col + dc[i]

                        if 0 <= test_r < H and 0 <= test_c < W:
                            if visited[test_r][test_c] == 0 and sand[test_r][test_c] == 0:
                                cnt += 1
                    if sand[row][col] <= cnt:
                        sand[row][col] = 0
                        visited[row][col] = 1
                        tot += 1

        if tot == 0:
            break

        chk += 1

    print("#{} {}".format(tc,chk))