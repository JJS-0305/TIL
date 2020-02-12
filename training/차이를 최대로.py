from itertools import permutations

N = int(input())

data = list(map(int, input().split()))

# print(data)

# 순열을 이용한 문제풀이
mx = 0
for i in permutations(data):
    tot = 0
    for j in range(1,N):
        tot += abs(i[j] - i[j-1])
    if tot > mx:
        mx = tot
        print(i, mx)

# N = int(input())
#
# data = list(map(int, input().split()))
# 정렬을 활용한 문제풀이
center = len(data)//2
data.sort()

result = [0] * len(data)
result[center] = data[-1]
data.pop(-1)
for i in range(1,N//2+1):
    if center + i > N-1:
        break
    if i % 2:
        result[center-i] = data[0]
        data.pop(0)
        result[center+i] = data[0]
        data.pop(0)
    else:
        result[center - i] = data[-1]
        data.pop(-1)
        result[center + i] = data[-1]
        data.pop(-1)
if len(data) == 1:
    result[0] = data[0]
tot = 0
for j in range(1,N):
    tot += abs(result[j] - result[j-1])
print(result, tot)