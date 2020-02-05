def iswall(x,y):
    if x < 0 or x >= N:
        return False
    if y < 0 or y >= N:
        return False
    return True

def danji(x,y):
    global cnt
    house[y][x] = 2
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        test_x = x + dx[i]
        test_y = y + dy[i]

        if iswall(test_x,test_y):
            if house[test_y][test_x] == 1:
                danji(test_x, test_y)
                cnt += 1

N = int(input())
house = [[0 for _ in range(N)] for _ in range(N)]
for row in range(N):
    house[row] = list(map(int, input()))
    # print(house[row])

cnt = 1
n = 0
result = []
for y in range(N):
    for x in range(N):
        if house[y][x] == 1:
            danji(x,y)
            n += 1
            result.append(cnt)
            cnt = 1

print(n)

result.sort()

for ans in result:
    print(ans)
