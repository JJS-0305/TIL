def perm(n,k,ans):
    global my_max
    if ans <= my_max:
        return
    if n == k:
        if ans > my_max:
            my_max = ans
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(n,k+1,ans*P[k][i]/100)
                visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    my_max = -1
    perm(N,0,100)
    print("#{} {}".format(tc,format(my_max,'.6f')))