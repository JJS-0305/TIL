from collections import deque
import sys
sys.stdin = open('연산_input.txt')

def operation(a,b):
    visited = [0] * 1000001
    queue = deque()
    queue.append(a)
    while queue:
        n = queue.popleft()
        if n == b:
            return visited[b]
        if n*2 < 1000001:
            if visited[n*2] == 0:
                visited[n*2] = visited[n] + 1
                queue.append(n*2)
        if n+1 < 1000001:
            if visited[n+1] == 0:
                visited[n+1] = visited[n] + 1
                queue.append(n+1)
        if n-1 > 0:
            if visited[n-1] == 0:
                visited[n-1] = visited[n] + 1
                queue.append(n-1)
        if n-10 > 0:
            if visited[n - 10] == 0:
                visited[n - 10] = visited[n] + 1
                queue.append(n - 10)
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    ans = operation(N,M,)
    print("#{} {}".format(tc,ans))