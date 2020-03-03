from _collections import deque

def bfs():
    chk = 0
    queue = deque()

    for row in range(H):
        for col in range(W):
            if sand[row][col] == '.':
                queue.append((row,col))
            else:
                sand[row][col] = int(sand[row][col])

    while True:
        tot = 0
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for i in range(8):
                test_r = r + dr[i]
                test_c = c + dc[i]

                if 0 <= test_r < H and 0 <= test_c < W:
                    if sand[test_r][test_c] != '.' and sand[test_r][test_c] != 0:
                        sand[test_r][test_c] -= 1
                        if sand[test_r][test_c] == 0:
                            queue.append((test_r,test_c))
                            tot += 1

        if tot == 0:
            break

        chk += 1

    return chk

dr = [1, -1, 1, -1, 1, -1, 0, 0]
dc = [0, 0, 1, 1, -1, -1, 1, -1]


T = int(input())

for tc in range(1,T+1):
    H, W = map(int, input().split())
    sand = [list(map(str, input())) for _ in range(H)]

    print("#{} {}".format(tc,bfs()))