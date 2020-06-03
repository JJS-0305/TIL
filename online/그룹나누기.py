import sys
sys.stdin = open('그룹나누기_input.txt')

def make_set(n):
    p[n] = n

def find_set(n):
    if p[n] == n:
        return p[n]
    else:
        return find_set(p[n])

def union(a,b):
    p[find_set(b)] = p[find_set(a)]


T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    apply = list(map(int, input().split()))
    p = [0] * (N+1)
    for i in range(1,N+1):
        make_set(i)
    for j in range(M):
        a, b = apply[j*2], apply[j*2+1]
        if a > b:
            a, b = b, a
        union(a,b)
    for k in range(N+1):
        p[k] = find_set(k)

    print("#{} {}".format(tc,len(set(p)) -1))

