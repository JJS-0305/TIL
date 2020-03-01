def perm(n,k):
    global my_max
    global my_min
    if n == k:
        ans = num[0]
        for j in range(n):
            if operation[j] == '+':
                ans += num[j+1]
            elif operation[j] == '-':
                ans -= num[j+1]
            elif operation[j] == '*':
                ans *= num[j+1]
            elif operation[j] == '/':
                ans /= num[j+1]
                ans = int(ans)
        if ans > my_max:
            my_max = ans
        if ans < my_min:
            my_min = ans
    else:
        for i in range(k,n):
            if k == 0 and i != 0 and operation[i] == operation[i-1]:
                continue
            else:
                operation[i], operation[k] = operation[k], operation[i]
                perm(n,k+1)
                operation[k], operation[i] = operation[i], operation[k]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt = list(map(int, input().split()))
    num = list(map(int, input().split()))

    operation = []
    for i in range(4):
        for _ in range(cnt[i]):
            if i == 0:
                operation.append('+')
            elif i == 1:
                operation.append('-')
            elif i == 2:
                operation.append('*')
            elif i == 3:
                operation.append('/')
    my_max = -987654321
    my_min = 987654321
    perm(N-1,0)
    print("#{} {}".format(tc, my_max - my_min))