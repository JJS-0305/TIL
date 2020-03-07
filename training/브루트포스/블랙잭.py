# 재귀
def comb(n,k,tot):
    global mx
    if n == k:
        if tot > mx:
            mx = tot
    else:
        for i in range(N):
            if A[i] == 0 and tot + card[i] <= M:
                A[i] = 1
                comb(n,k+1,tot+card[i])
                A[i] = 0

N, M = map(int, input().split())
card = list(map(int, input().split()))
A = [0] * (N+1)
mx = 0
comb(3,0,0)
print(mx)

# 브루트 포스
mx2 = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            tot2 = card[i] + card[j] + card[k]
            if tot2 <= M and tot2 > mx2:
                mx2 = tot2
print(mx2)