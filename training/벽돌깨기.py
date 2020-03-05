from copy import copy

def crush(ls):
    for c in range(W):
        for r in range(H):
            if ls[c][r] != 0:
                pass

                break

T = int(input())

for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    # for i in range(H):
    #     print(brick[i])
    # print()
