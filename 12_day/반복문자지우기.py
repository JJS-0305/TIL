import sys
sys.stdin = open("반복문자지우기_input.txt")

T = int(input())

for tc in range(T):
    str1 = input()
    stack = []
    for i in str1:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    print("#{} {}".format(tc+1,len(stack)))