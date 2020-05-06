import sys
sys.stdin = open('이진수2_input.txt')

T = int(input())

for tc in range(1,T+1):
    n = float(input())
    b = 1
    answer = []
    while True:
        b /= 2
        if n == 0:
            break
        if b < 2**(-13):
            answer = 'overflow'
            break
        if n >= b:
            answer.append('1')
            n -= b
        else:
            answer.append('0')

    print("#{} {}".format(tc,''.join(answer)))