

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    result = []

    for i in range(N):
        for j in range(i+1, N):
            result.append(str(num[i] * num[j]))
    # print(result)

    for k in range(len(result)):
        for l in range(len(result[k])-1):
            if result[k][l] > result[k][l+1]:
                result[k] = 0
                break

    # print(result)
    result = list(map(int, result))
    # print(result)
    mx = 0
    for a in result:
        if a > mx:
            mx = a
    if mx == 0:
        print("#{} -1".format(tc + 1))
    else:
        print("#{} {}".format(tc + 1, mx))