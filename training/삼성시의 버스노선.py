T = int(input())

for tc in range(T):
    stop = [0] * 5001
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            stop[j] += 1
    P = int(input())

    print("#{} ".format(tc+1), end="")
    for _ in range(P):
        c = int(input())
        print(stop[c],end=" ")
    print()