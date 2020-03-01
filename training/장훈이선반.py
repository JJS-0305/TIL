def printset(n):
    sum = 0
    for i in range(n):
        if A[i] == 1:
            sum += H[i]
    return sum
def powerset(n,k,B):
    if printset(n) >= B:
        result.append(printset(n))
        return
    elif n != k:
        A[k] = 1
        powerset(n,k+1,B)
        A[k] = 0
        powerset(n,k+1,B)


T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for _ in range(N)]
    result = []

    powerset(N,0,B)
    print("#{} {}".format(tc+1,min(result)-B))