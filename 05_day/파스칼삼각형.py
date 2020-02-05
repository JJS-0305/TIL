T = int(input())

for tc in range(T):
    N = int(input())
    ls = [[0] * i for i in range(1, N + 1)]
    print(ls)

    # 각 행의 처음과 끝에 1 삽입
    for i in range(len(ls)):
        ls[i][0] = 1
        if len(ls[i]) != 1:
            ls[i][-1] = 1
    print(ls)

    for j in range(len(ls)):
        for k in range(len(ls[j])):
            if ls[j][k] == 0:
                ls[j][k] = ls[j-1][k-1] + ls[j-1][k]

    print("#{}".format(tc+1))
    for a in range(len(ls)):
        for b in range(len(ls[a])):
            print(ls[a][b], end=" ")
        print()