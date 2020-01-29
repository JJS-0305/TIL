tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    pali = [[0]*n for i in range(n)]
    for i in range(n):
        pali[i] = list(map(str,input()))
    for row in range(n):
        for col in range(n-m+1):
            if pali[row][col:col+m] == pali[row][col:col+m][::-1]:
                print("#{} {}".format(t+1,''.join(pali[row][col:col+m])))

    t_pali = list(zip(*pali))
    print(t_pali)

    # for row in range(n):
    #     for col in range(n - m + 1):
    #         if t_pali[row][col:col + m] == t_pali[row][col:col + m][::-1]:
    #             print("#{} {}".format(t + 1, ''.join(t_pali[row][col:col + m])))