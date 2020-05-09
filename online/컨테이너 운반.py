import sys
sys.stdin = open('컨테이너운반_input.txt')

def mx_move(lst_a, lst_b):
    tot = 0
    for i in range(N):
        for j in range(M):
            if lst_a[i] <= lst_b[j]:
                tot += lst_a[i]
                lst_b[j] = 0
                break
    return tot
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    ans = mx_move(container,truck)
    print("#{} {}".format(tc,ans))