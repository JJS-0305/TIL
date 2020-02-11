import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print("#{} 1".format(tc+1))
    else:
        print("#{} 0".format(tc+1))