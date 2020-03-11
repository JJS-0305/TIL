N = int(input())
x = [0] * N
y = [0] * N
rank = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if x[i] < x[j] and y[i] < y[j]:
            cnt += 1
    rank[i] = cnt
print(*rank)