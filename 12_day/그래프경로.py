import sys
sys.stdin = open("그래프경로_input.txt")

def route(S,G):
    result = []
    chk = [0] * E
    idx = s.index(S)
    result.append(S)
    result.append(g[idx])
    chk[idx] = 1
    while len(result) > 0:
        for j in range(len(s)):
            if result[-1] == G:
                return 1
            elif result[-1] == s[j] and chk[j] == 0:
                result.append(g[j])
                chk[j] = 1
                break
        else:
            result.pop()
    return 0

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    s = [0] * E
    g = [0] * E
    for i in range(E):
        s[i], g[i] = map(int, input().split())
    S, G = map(int, input().split())
    print("#{} {}".format(tc+1, route(S,G)))
