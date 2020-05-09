# 에라토스테네스의 체
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 자기보다 작은 소수의 배수가 아니면 소수이다.
def solution2(n):
    answer = 1
    memo = []
    for i in range(3,n+1,2):
        for j in memo:
            if i % j == 0:
                break
            # 루트 n 까지의 소수만 비교해도 충분하다.(수학적으로 증명됨)
            if j**2 > i:
                memo += [i]
                answer += 1
                break
        else:
            memo += [i]
            answer += 1
    return answer