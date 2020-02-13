def fibo2(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-2) + fibo2(n-1))

    return memo[n]

memo = [0,1]

print(fibo2(500))