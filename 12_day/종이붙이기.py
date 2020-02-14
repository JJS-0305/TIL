import sys
sys.stdin = open("종이붙이기_input.txt")

def dp(N):
    memo = [0,1,3]
    for i in range(3, N//10 +1):
        memo.append(memo[i-1] + memo[i-2]*2)

    return(memo[N//10])

T = int(input())

for tc in range(T):
    N = int(input())

    print("#{} {}".format(tc+1,dp(N)))