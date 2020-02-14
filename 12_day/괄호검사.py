import sys
sys.stdin = open("괄호검사_input.txt")

def blacket_chk(string):
    stack = []
    for i in str1:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif i == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if len(stack) > 0:
        return 0
    return 1

T = int(input())

for tc in range(T):
    str1 = input()
    ans = blacket_chk(str1)

    print("#{} {}".format(tc+1, ans))