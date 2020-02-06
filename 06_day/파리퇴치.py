T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    fly = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        fly[i] = list(map(int, input().split()))
    # print(fly)

    mx = 0
    for j in range(N-M+1):
        for k in range(N-M+1):
            tot = 0
            for l in range(M):
                for m in range(M):
                    tot += fly[j+l][k+m]
                    # print(fly[j+l][k+m])
                    # print(tot)
            if tot > mx:
                mx = tot
    print("#{} {}".format(tc+1,mx))