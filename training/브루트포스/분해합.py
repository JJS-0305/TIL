N = int(input())

cnt = 0
n = N
# 자리수 확인
while n > 0:
    cnt += 1
    n //= 10

# 생성자 찾기
for i in range(N-9*cnt, N):
    decomposition = i
    constructor = i
    for _ in range(cnt):
        constructor += decomposition % 10
        decomposition //= 10
    # print(i, constructor)
    if constructor == N:
        print(i)
        break
else:
    print(0)