N = 10
data = list(range(1,11))
A = [0 for _ in range(N)]

def printset(n):
    result = []
    for i in range(n):
        if A[i] == 1:
            result.append(data[i])
    return result

def powerset(n,k,total):
    ans = []
    if n == k:
        if sum(printset(n)) == total:
            print(printset(n))
    else:
        A[k] = 1
        powerset(n,k+1,total)
        A[k] = 0
        powerset(n,k+1,total)

powerset(N,0,10)