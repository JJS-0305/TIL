T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    center = (N-1)//2
    total = 0
    for i in range(N):
        total += int(data[i][center])
        if i <= center:
            for j in range(1,i+1):
                total += int(data[i][center-j]) + int(data[i][center+j])
                # print(j, total)
        else:
            k = N - 1 - i
            for j in range(1,k+1):
                total += int(data[i][center-j]) + int(data[i][center+j])
                # print(total)
    print("#{} {}".format(tc+1,total))