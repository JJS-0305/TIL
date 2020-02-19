import sys
sys.stdin = open("Forth_input.txt")

def calculator(s):
    operator = '+-*/'
    # print(type(s[0]))
    while(1):
        for i in range(len(s)):
            if i != len(s)-1 and s[i] == '.':
                return 'error'
            elif str(s[i]) in operator:
                if i < 2:
                    return 'error'
                elif s[i] == '+':
                    s[i-2] = int(s[i-2]) + int(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break
                elif s[i] == '-':
                    s[i-2] = int(s[i-2]) - int(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break
                elif s[i] == '*':
                    s[i-2] = int(s[i-2]) * int(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break
                elif s[i] == '/':
                    s[i-2] = int(s[i-2]) // int(s[i-1])
                    s.pop(i)
                    s.pop(i-1)
                    break
            elif s[i] == '.' and i == len(s)-1:
                if len(s) == 2:
                    return s[i-1]
                else:
                    return 'error'

'''
1
10 2 + 3 4 + * .
'''
T = int(input())

cal = []
for tc in range(T):
    cal = list(map(str, input().split()))
    # print(type(cal[1]))
    print("#{} {}".format(tc+1,calculator(cal)))