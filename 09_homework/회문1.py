T = 10

for tc in range(T):
    N = int(input())
    data = [list(input()) for _ in range(8)]

    cnt = 0
    # 가로 회문 찾기
    for r in range(8):
        for st in range(8-N+1):
            for c in range(N):
                if data[r][st+c] != data[r][st+N-1-c]:
                    break
            else:
                cnt += 1

    #전치
    data2 = list(zip(*data))

    #세로 회문 찾기
    for r in range(8):
        for st in range(8-N+1):
            for c in range(N):
                if data2[r][st+c] != data2[r][st+N-1-c]:
                    break
            else:
                cnt += 1

    print("#{} {}".format(tc+1,cnt))