import sys
sys.stdin = open('최적경로_input.txt')

def mn_dist(n,r,d,x,y):
    global mn

    if d > mn:
        return
    if n == r:
        d += abs(x-ls[1][0]) + abs(y-ls[1][1])
        if d < mn:
            mn = d
        return
    else:
        for i in range(2,N+2):
            if visited[i] == 0:
                visited[i] = 1
                d2 = d+ abs(x-ls[i][0]) + abs(y-ls[i][1])
                mn_dist(n,r+1,d2,ls[i][0], ls[i][1])
                visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    xy = list(map(int, input().split()))
    visited = [0] * (N+2)

    ls = []
    for i in range(0,len(xy),2):
        ls.append((xy[i],xy[i+1]))

    mn = 100*(N+2)
    mn_dist(N,0,0,ls[0][0], ls[0][1])
    print("#{} {}".format(tc,mn))