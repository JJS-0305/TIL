import sys
sys.stdin = open("회전_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for _ in range(M):
        data = queue.pop(0)
        queue.append(data)

    print("#{} {}".format(tc+1,queue[0]))