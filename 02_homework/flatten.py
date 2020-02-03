def mx(data):
    mx = 0
    for i in range(len(data)):
        if data[i] > data[mx] :
            mx = i

    return mx

def mn(data):
    mn = 0
    for i in range(len(data)):
        if data[i] < data[mn]:
            mn = i

    return mn

T = 10

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N):
        data[mx(data)] -= 1
        data[mn(data)] += 1

    result = data[mx(data)] - data[mn(data)]

    print("#{} {}".format(tc+1, result))