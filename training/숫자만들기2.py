def perm(n,k,plus,minus,mul,div,ans):
    # print(plus, minus, mul, div, ans)
    global my_max
    global my_min
    if k == 0:
        ans = num[0]
    if n == k:
        if ans > my_max:
            my_max = ans
        if ans < my_min:
            my_min = ans
    else:
        if plus != 0:
            ans += num[k+1]
            perm(n, k+1, plus-1, minus, mul, div,ans)
            ans -= num[k+1]
        if minus != 0:
            ans -= num[k + 1]
            perm(n, k + 1, plus, minus-1, mul, div,ans)
            ans += num[k+1]
        if mul != 0:
            ans *= num[k + 1]
            perm(n, k + 1, plus, minus, mul-1, div,ans)
            ans /= num[k+1]
            ans = int(ans)
        if div != 0:
            ans /= num[k+1]
            perm(n, k + 1, plus, minus, mul, div-1,int(ans))
            ans *= num[k+1]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    num = list(map(int, input().split()))

    my_max = -987654321
    my_min = 987654321
    perm(N-1,0,plus,minus,mul,div,0)
    print("#{} {}".format(tc,my_max - my_min))