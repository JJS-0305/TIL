T = int(input())

for tc in range(1,T+1):
    N = int(input())
    corridor = [0] * 200
    for i in range(N):
        st, ed = map(int, input().split())
        if st % 2:
            st //= 2
        else:
            st -= 1
            st //= 2
        if ed % 2:
            ed //= 2
        else:
            ed -= 1
            ed //= 2

        mx = max(st,ed)
        mn = min(st,ed)
        for j in range(mn,mx+1):
            corridor[j] += 1

    print("#{} {}".format(tc,max(corridor)))