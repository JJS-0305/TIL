# [i][j] = i번째에 j가 될수있는 경우의 수
# [i][j] = [i-1][0~20] + d[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int,input().split()))
    dp_list = [[0 for _ in range(21)] for _ in range(N-1)]
    dp_list[0][num[0]] += 1

    for i in range(1,N-1):
        for j in range(21):
            if dp_list[i-1][j] != 0:
                if j - num[i] >= 0:
                    dp_list[i][j-num[i]] += dp_list[i-1][j]
                if j + num[i] <= 20:
                    dp_list[i][j + num[i]] += dp_list[i - 1][j]

    ans = dp_list[N-2][num[N-1]]%1234567891
    print("#{} {}".format(tc,ans))