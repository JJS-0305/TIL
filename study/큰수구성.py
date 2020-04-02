def comb(k,num):
    global mx
    if num > N:
        return
    elif k == 0:
        if num > mx:
            mx = num
    else:
        for i in range(K):
            comb(k-1,num + k_list[i]*10**(k-1))


N, K = map(int, input().split())
k_list = list(map(int,input().split()))
mx = 0
comb(len(str(N)),0)

if mx == 0:
    mx = str(max(k_list))*(len(str(N))-1)
    print(int(mx))
else : print(mx)