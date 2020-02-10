import sys
sys.stdin = open("GNS_input")

def my_count(data):
    dic = {}
    for i in range(len(data)):
        if data[i] not in dic:
            dic[data[i]] = dic.get(data[i],0) + 1
        else:
            dic[data[i]] += 1

    return dic

T = int(input())

for tc in range(T):
    N = list(map(str, input().split()))
    data = list(map(str,input().split()))
    dic = my_count(data)
    result = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print("#{} ".format(tc+1))
    ans = ''
    for char in result:
        ans += (char + ' ') * dic[char]
    print(ans)