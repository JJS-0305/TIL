def rotation(data, cnt):
    data2 = data[::]
    while cnt > 0 :
        for i in range(N//2):
            data2[i], data2[-i-1] = data2[-i-1], data2[i]
        data2 = list(map(list, zip(*data2)))
        cnt -= 1

    return data2

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]

    print("#{}".format(tc+1))
    for j in range(N):
        print(''.join(rotation(data, 1)[j]), end=" ")
        print(''.join(rotation(data, 2)[j]), end=" ")
        print(''.join(rotation(data, 3)[j]), end=" ")
        print()