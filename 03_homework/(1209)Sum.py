import sys
sys.stdin = open("(1209)Sum_input.txt")
T = 10

for tc in range(T):
    no = int(input())
    data = [[0 for _ in range(100)]for _ in range(100)]
    for i in range(100):  # 입력
        data[i] = list(map(int, input().split()))

    # data = [list(map(int, input().split())) for _ in range(100)]
    max = 0
    for i in range(100):  #row
        temp = 0
        for j in range(100):
            temp += data[i][j]
        if temp > max:
            max = temp

    for i in range(100):  # col
        temp = 0
        for j in range(100):
            temp += data[j][i]
        if temp > max:
            max = temp

    temp = 0
    for i in range(100):  # dia1
        temp += data[i][i]
    if temp > max:
        max = temp

    temp = 0
    for i in range(100):  # dia2
        temp += data[i][99-i]
    if temp > max:
        max = temp

    print("#{} {}".format(no, max))