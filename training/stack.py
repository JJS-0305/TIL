import sys
sys.stdin = open("stack_input")

T = int(input())

for tc in range(T):
    str = list(input())
    # print(str)

    while True:
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                str.pop(i+1)
                str.pop(i)
                break
        else:
            # print(str)
            break

    print("#{} {}".format(tc+1, len(str)))