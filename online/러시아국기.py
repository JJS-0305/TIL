def perm(ls,k):
    if k == N-2 and ls[k-1] == 'W':
        ls[k] = 'B'
        perm(ls,k+1)
    elif k == N-1:
        ls[k] = 'R'
        find_min(ls)
        return
    else:
        if ls[k-1] == 'W':
            ls[k] = 'W'
            perm(ls,k+1)
            ls[k] = 'B'
            perm(ls,k+1)
        elif ls[k-1] == 'B':
            ls[k] = 'B'
            perm(ls,k+1)
            ls[k] = 'R'
            perm(ls,k+1)
        elif ls[k-1] == 'R':
            ls[k] = 'R'
            perm(ls,k+1)
def find_min(ls):
    global my_min
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_list[i][j] != ls[i]:
                cnt += 1
        if cnt > my_min:
            return
    if cnt < my_min:
        my_min = cnt

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    map_list = [list(input()) for _ in range(N)]
    cnt = 0

    A = [0] * N
    A[0] = 'W'

    my_min = 987654321
    perm(A,1)
    print("#{} {}".format(tc,my_min))