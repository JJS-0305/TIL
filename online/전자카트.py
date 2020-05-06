import sys
sys.stdin = open('전자카트_input.txt')

def perm(N,r,st):
    global tot
    global ans
    if N == r:
        if tot < ans:
            ans = tot
        return
    else:
        for i in range(N):
            if i==0 and r != N-1:
                continue
            elif visited[i] == 0:
                visited[i] = 1
                tot += battery[st][i]
                perm(N,r+1,i)
                tot -= battery[st][i]
                visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0] * N
    tot = 0
    perm(N,0,0)
    print("#{} {}".format(tc,ans))