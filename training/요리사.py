def comb(n,k):
    global my_min
    if k == n/2:
        sum1 = 0
        sum2 = 0
        for i in range(N):
            if visited[i] == 1:
                for j in range(i+1,N):
                    if visited[j] == 1:
                        sum1 += S[i][j]
                        sum1 += S[j][i]
            elif visited[i] == 0:
                for k in range(i+1,N):
                    if visited[k] == 0:
                        sum2 += S[i][k]
                        sum2 += S[k][i]
        ans = sum1 - sum2
        if ans < 0:
            ans *= -1
        if ans < my_min:
            my_min = ans
        return
    else:
        for i in range(k,N):
            if visited[i] == 0:
                visited[i] = 1
                comb(n,k+1)
                visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    my_min = 987654321
    comb(N,0)
    print("#{} {}".format(tc,my_min))