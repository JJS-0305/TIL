T = 10

for tc in range(T):
    V, E = map(int,input().split())

    data = list(map(int, input().split()))


    ls = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    for i in range(0, len(data), 2):
        start = data[i]
        end = data[i+1]
        ls[start][end] = 1

    visited = [0] * (V+1)
    result = []
    while True:
        count = [0] * (V + 1)
        for j in range(1,V+1):
            for i in range(1,V+1):
                if ls[i][j] == 1:
                    count[j] += 1

        # for i in range(len(ls)):
        #     print(ls[i])
        # print()
        #
        # print(count)
        # print()

        for i in range(1,V+1):
            if count[i] == 0 and visited[i] == 0:
                result.append(i)
                visited[i] = 1
                for j in range(1,V+1):
                    ls[i][j] = 0
        #
        # print()

        if len(result) == V:
            break

    print("#{}".format(tc+1), *result)