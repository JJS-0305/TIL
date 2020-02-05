T = 10
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(100) ] for _ in range(100)]
    sum_list = []
    for i in range(100):
        arr[i] = list(map(int, input().split()))



    for j in range(100):
        tot = 0
        tot2 = 0
        for k in range(100):
            tot += arr[j][k]
            if j == k:
                tot2 += arr[j][k]
        sum_list.append(tot)
    sum_list.append(tot2)

    for r in range(len(arr)):
        for c in range(r + 1, len(arr[r])):
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]

    for jj in range(100):
        tot = 0
        tot2 = 0
        for kk in range(100):
            tot += arr[jj][kk]
<<<<<<< HEAD
            if jj == kk:
=======
            if jj + kk == 99 :
>>>>>>> origin/master
                tot2 += arr[jj][kk]
        sum_list.append(tot)
    sum_list.append(tot2)

    mx = 0
    for num in sum_list:
        if num > mx:
            mx = num

    print("#{} {}".format(tc+1,mx))

