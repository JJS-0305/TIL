def make_table(keyword, table):
    table[0] = 0

    i = 1
    cnd = 0

    while i < len(keyword):
        if keyword[i] == keyword[cnd]:
            cnd += 1
            table[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = table[cnd-1]
        else:
            table[i] = 0
            i += 1

def kmp(keyword, table, reference):
    cnt = 0

    k = 0
    r = 0
    len_k = len(keyword)
    len_r = len(reference)

    while r < len_r:
        if keyword[k] == reference[r]:
            k += 1
            r += 1
            if k == len_k:
                cnt += 1
                k = table[k-1]
        else:
            if k:
                k = table[k-1]
            else:
                r += 1
    return cnt

def GCD(a,b):
    if a < b:
        a,b = b,a

    while b != 0:
        n = a % b
        a = b
        b = n
    return a


N = int(input())

keyword = list(input().split())
reference = list(input().split())

table = [0] * N
make_table(keyword,table)
ans = kmp(keyword,table,reference+reference[:-1])
G = GCD(N,ans)
print("{}/{}".format(ans//G,N//G))