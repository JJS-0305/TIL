import sys
sys.stdin = open("view_input.txt")

T = 10

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for i in range(2,N-2):
        nb1 = 0
        nb2 = 0
        if data[i-1] > data[i-2]:
            nb1 = data[i-1]
        else :
            nb1 = data[i-2]
        if data[i+1] > data[i+2]:
            nb2 = data[i+1]
        else :
            nb2 = data[i+2]
        if data[i] > nb1 and data[i] > nb2:
            if nb1 > nb2:
                cnt += data[i] - nb1
            else:
                cnt += data[i] - nb2
    print("#{} {}".format(tc+1, cnt))


