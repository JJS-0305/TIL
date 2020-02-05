import sys
sys.stdin = open("input.txt")
# 모든 막대는 다 연결된다
T = int(input())

for tc in range(T):
    front = []
    end = []
    result = []
    N = int(input())
    data = list(map(int,input().split()))
    for i in range(len(data)):
        if i % 2:
            end.append(data[i])
        else:
            front.append(data[i])

    #start point 찾기
    for j in range(len(front)):
        if front[j] not in end:
            result.append(front[j])
            result.append(end[j])
            break

    while len(result) < 2*N:
        for k in range(N):
            if result[-1] == front[k]:
                result.append(front[k])
                result.append(end[k])
    `
    print("#{} {}".format(tc+1, ' '.join(map(str, result))))