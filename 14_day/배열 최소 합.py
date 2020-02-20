import sys
sys.stdin = open("배열최소합_input.txt")
def perm(n,k):
    global result
    if k != n:
        sum = 0
        for i in range(k):
            sum += data[i][arr[i]]
            if sum > result:
                return
    if k == n:
        sum = 0
        for i in range(N):
            sum += data[i][arr[i]]
        if sum < result:
            result = sum
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

T = int(input())

for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    result = 10*N
    perm(N,0)
    # print(result)
    print("#{} {}".format(tc+1,result))