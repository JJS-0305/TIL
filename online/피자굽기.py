import sys
sys.stdin = open("피자굽기_input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    cheese = list(map(int, input().split()))

    queue = []
    idx = 1
    for _ in range(N):
        queue.append([cheese.pop(0),idx])
        idx += 1

    while queue:
        data = queue.pop(0)
        data[0] = data[0]//2
        if data[0] == 0:
            if len(cheese) != 0:
                queue.append([cheese.pop(0), idx])
                idx += 1
        else:
            queue.append(data)

        if len(queue) == 1:
            ans = queue[0][1]
            break

    print("#{} {}".format(tc+1, ans))