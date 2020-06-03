from collections import deque
import copy

import sys
sys.stdin = open('최대상금_input.txt')

def money(num, change):
    global result
    num = list(str(num))
    queue = deque()
    cnt = 0
    queue.append((num, cnt))

    while queue:
        number, cnt = queue.popleft()
        if cnt == change:
            break
        for i in range(len(number)):
            for j in range(i, len(number)):
                if i != j:
                    number[i], number[j] = number[j], number[i]
                    n = int(''.join(number))
                    if n not in result[cnt+1]:
                        result[cnt + 1].append(n)
                        queue.append((number.copy(), cnt + 1))
                    number[i], number[j] = number[j], number[i]
T = int(input())

for tc in range(1, T + 1):
    num, change = map(int, input().split())
    result = [[] for _ in range(change+1)]
    result[0].append(num)
    money(num, change)
    # print(result)
    print("#{} {}".format(tc,max(result[-1])))