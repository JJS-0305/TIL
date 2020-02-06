'''
1
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''
T = int(input())


for tc in range(T):
    string = [[0] for _ in range(5)]
    for i in range(5):
        string[i] = list(map(str, input()))

    print("#{} ".format(tc+1),end="")
    for i in range(15):
        for j in range(5):
            if len(string[j]) <= i:
                continue
            else:
                print(string[j][i], end ="")

    print()