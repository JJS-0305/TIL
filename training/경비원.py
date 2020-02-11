width, height = map(int, input().split())
N = int(input())

dir = [0] * (N+1)
distance = [0] * (N+1)
for i in range(N+1):
    dir[i], distance[i] = map(int, input().split())

location = []

for j in range(N+1):
    if dir[j] == 1:
        location.append((0,distance[j]))
    elif dir[j] == 2:
        location.append((height,distance[j]))
    elif dir[j] == 3:
        location.append((distance[j],0))
    elif dir[j] == 4:
        location.append((distance[j],width))
# print(location)

sum = 0
for k in range(N):
    if dir[N] == dir[k]:
        sum += abs(distance[N] - distance[k])
    else:
        sum += abs(location[N][0] - location[k][0]) + abs(location[N][1] - location[k][1])
        sum += min(min(location[N][0],location[k][0]),height - max(location[N][0],location[k][0])) * 2
        sum += min(min(location[N][1],location[k][1]),width - max(location[N][1],location[k][1])) * 2
print(sum)