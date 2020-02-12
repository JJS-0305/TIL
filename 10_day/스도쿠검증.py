def validation(data):
    #가로 체크
    for i in range(9):
        dic = {}
        for j in range(9):
            dic[data[i][j]] = dic.get(data[i][j],0) + 1
        if len(dic.values()) != 9:
            return 0

    data2 = list(zip(*data))

    #세로 체크
    for i in range(9):
        dic = {}
        for j in range(9):
            dic[data2[i][j]] = dic.get(data2[i][j],0) + 1
        if len(dic.values()) != 9:
            return 0

    # 박스 나누기
    ls = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            ls.append(data[i][j:j+3])
            ls.append(data[i+1][j:j+3])
            ls.append(data[i+2][j:j+3])

    #박스 체크
    k = 3
    while True:
        result = []
        for i in range(k-3,k):
            for j in range(3):
                result.append(ls[i][j])
        result = set(result)
        if len(result) != 9:
            return 0
        k += 3
        if k > len(ls):
            break

    return 1

T = int(input())

for tc in range(T):
    data = [list((input().split())) for _ in range(9)]
    # for i in range(9):
        # print(data[i])
    print("#{} {}".format(tc+1,validation(data)))
