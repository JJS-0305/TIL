import sys
sys.stdin = open('화물 도크_input.txt')

def dfs(st, cnt):
    global mx
    for i in range(st,24):
        if se[i] != 0:
            cnt += 1
            dfs(se[i],cnt)
            cnt -= 1
    if cnt > mx:
        mx = cnt

T = int(input())

for tc in range(1,T+1):
    se = [0] * 24
    N = int(input())
    for _ in range(N):
        s,e = map(int, input().split())
        if se[s]:
            if se[s] > e:
                se[s] = e
        else:
            se[s] = e
    mx = 0
    for i in range(24):
        if se[i] != 0:
            dfs(i, 0)
    print("#{} {}".format(tc, mx))