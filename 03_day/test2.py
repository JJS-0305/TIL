#부분집합 합
def partsum_ten(n):

    for i in range(1 << len(n)):
        tot = 0
        result = []
        for j in range(len(n)):
            if i & (1<<j):
                tot += n[j]
                result.append(n[j])
        if tot == 10:
            print(result)

arr = list(range(1,11))
partsum_ten(arr)