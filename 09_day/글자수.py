import sys
sys.stdin = open("글자수_input.txt")

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    str1 = list(set(str1))

    dic_count = {}
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dic_count[str1[i]] = dic_count.get(str1[i],0) + 1

    print("#{} {}".format(tc+1,max(dic_count.values())))