# 2차배열 이웃합
'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
def iswall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

tot = 0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if iswall(testX, testY) == False:
                tot += abs(arr[testY][testX] - arr[y][x])

print(tot)

