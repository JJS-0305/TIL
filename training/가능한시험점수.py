T = int(input())

for tc in range(1,T+1):
    N = int(input())
    score = sorted(list(map(int, input().split())))
    A = [0] * N
    max_score = sum(score)
    possible = [0] * (max_score+1)
    possible[0] = 1

    queue = []
    queue.append(0)
    pos = 0     #현재 위치

    cnt = 1     #가능한 개수
    while pos < N:
        temp = []
        for val in queue:
            if possible[val + score[pos]] == 0:
                possible[val + score[pos]] = 1
                temp.append(val + score[pos])
                cnt += 1
        pos += 1
        queue += temp

    print("#{} {}".format(tc,cnt))