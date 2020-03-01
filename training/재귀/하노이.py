def hanoi(n,start,waypoint,destination):
    global cnt
    global memo
    if n == 0:
        return

    hanoi(n-1,start,destination,waypoint)
    cnt += 1
    memo.append([start,destination])
    hanoi(n-1,waypoint,start,destination)


N = int(input())
cnt = 0
memo = []
hanoi(N,1,2,3)
print(cnt)
for i in range(len(memo)):
    print(*memo[i])
