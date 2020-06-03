import sys
sys.stdin = open('최소생산비용_input.txt')

def min_cost(n,r,cost):
    global mn
    if cost > mn:
        return
    if n == r:
        if cost < mn:
            mn = cost
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                cost += V[r][i]
                min_cost(n,r+1,cost)
                visited[i] = 0
                cost -= V[r][i]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    V = [0] * N
    for i in range(N):
        V[i] = list(map(int, input().split()))

    visited = [0] * N
    mn = 99 * N
    min_cost(N,0,0)
    print("#{} {}".format(tc,mn))