from collections import deque

def move(st_r,st_c,ed_r,ed_c):
    distance = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[0 for _ in range(l)] for _ in range(l)]
    que_r = deque()
    que_c = deque()
    que_r.append(st_r)
    que_c.append(st_c)
    while True:
        # print(que_r)
        # print(que_c)
        if que_r[0] == ed_r and que_c[0] == ed_c:
            print(distance[ed_r][ed_c])
            break
        for i in range(8):
            test_r = que_r[0] + dr[i]
            test_c = que_c[0] + dc[i]

            if 0 <= test_r < l and 0 <= test_c < l:
                if visited[test_r][test_c] == 0:
                    que_r.append(test_r)
                    que_c.append(test_c)
                    visited[test_r][test_c] = 1
                    distance[test_r][test_c] = distance[que_r[0]][que_c[0]] + 1

        que_r.popleft()
        que_c.popleft()

dr = [2,-2,1,-1,-2,2,-1,1]
dc = [1,-1,2,-2,1,-1,2,-2]

T = int(input())

for tc in range(T):
    l = int(input())
    st_r, st_c = map(int, input().split())
    ed_r, ed_c = map(int, input().split())

    move(st_r,st_c,ed_r,ed_c)