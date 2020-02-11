T = 10

for i in range(T):
    tc = int(input())
    data = [list(input()) for _ in range(100)]

    mx = 1
    # 가로 회문 찾기
    for N in range(2,101):
        for r in range(100):
            if N <= mx:
                break
            for st in range(100-N+1):
                for c in range(N):
                    if data[r][st+c] != data[r][st+N-1-c]:
                        break
                else:
                    mx = N
                    break
    #전치
    data2 = list(zip(*data))

    for N in range(2,101):
        if N <= mx:
            continue
        for r in range(100):
            if N <= mx:
                break
            for st in range(100-N+1):
                for c in range(N):
                    if data2[r][st+c] != data2[r][st+N-1-c]:
                        break
                else:
                    mx = N
                    break
    print("#{} {}".format(tc,mx))