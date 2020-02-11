N = int(input())

P = list(map(int, input().split()))
S = list(map(int, input().split()))
card = list(range(N))
result = [0] * N
result = card[::]
cnt = 0
while True:
    for k in range(N):
        if P[result[k]] != k%3:
            break
    else:
        print(cnt)
        break
    cnt += 1
    for i in range(len(S)):
        result[S[i]] = card[i]
    # print(result)
    card = result[::]

    if result == list(range(N)):
        print(-1)
        break