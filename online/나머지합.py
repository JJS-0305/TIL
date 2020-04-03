N, M = map(int, input().split())
num = list(map(int,input().split()))
memo = [0 for _ in range(N)]    # 처음부터 index번호까지 숫자의 합을 M으로 나눈 나머지
memo2 = [0 for _ in range(M)]   # M으로 나눈 나머지 개수 count
cnt = 0
for i in range(N):
    if i == 0:
        memo[i] = num[i]
    else:
        memo[i] = memo[i-1] + num[i]

    memo[i] %= M

for i in range(N):
    memo2[memo[i]] += 1
cnt += memo2[0]

for j in range(M):
    if memo2[j] >= 2:
        cnt += memo2[j] * (memo2[j]-1) // 2

print(cnt)