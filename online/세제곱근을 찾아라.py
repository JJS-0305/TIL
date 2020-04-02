T = int(input())

for tc in range(1,T+1):
    N = int(input())
    x = round(pow(N, 1/3))
    if pow(x,3) == N:
        print("#{} {}".format(tc, x))
    else:
        print("#{} {}".format(tc, -1))