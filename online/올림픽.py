T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    vote = [0] * N

    for i in range(M):
        for j in range(N):
            if A[j] <= B[i]:
                vote[j] += 1
                break

    ans = 0
    my_max = 0
    for i in range(N):
        if vote[i] > my_max:
            my_max = vote[i]
            ans = i+1

    print("#{} {}".format(tc,ans))