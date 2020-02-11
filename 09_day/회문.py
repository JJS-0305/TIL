import sys
sys.stdin = open("회문_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]

    for row in range(N):
        for start in range(N-M+1):
            for col in range(M//2):
                if data[row][start + col] != data[row][start + M -col-1]:
                    break
            else:
                print("#{} {}".format(tc+1,''.join(data[row][start:start+M])))

    data2 = list(zip(*data))

    for row in range(N):
        for start in range(N-M+1):
            for col in range(M//2):
                if data2[row][start + col] != data2[row][start + M -col-1]:
                    break
            else:
                print("#{} {}".format(tc+1,''.join(data2[row][start:start+M])))
