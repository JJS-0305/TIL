def min_route(x1,y1,x2,y2):
    gap_x = x1-x2
    gap_y = y1-y2

    if gap_x * gap_y >= 0:
        return max(abs(gap_x), abs(gap_y))
    else:
        return abs(gap_x) + abs(gap_y)

T = int(input())

for tc in range(1,T+1):
    W, H, N = map(int, input().split())
    xy = [0] * N

    for i in range(N):
        xy[i] = list(map(int, input().split()))

    cnt = 0
    for i in range(1,N):
        cnt += min_route(xy[i-1][0], xy[i-1][1], xy[i][0], xy[i][1])

    print("#{} {}".format(tc, cnt))