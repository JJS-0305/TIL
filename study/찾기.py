def kmp_table(pattern, table):
    table[0] = 0

    i = 1
    cnd = 0

    while (i < len(pattern)):
        if pattern[i] == pattern[cnd]:
            cnd += 1
            table[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = table[cnd-1]
        else:
            table[i] = 0
            i += 1

def kmp(pattern, table, reference):
    index = []
    r = 0
    p = 0
    len_r = len(reference)
    len_p = len(pattern)
    while r < len_r:
        if pattern[p] == reference[r]:
            p += 1
            r += 1
            if p == len_p:
                index.append(r-p+1)
                p = table[p-1]
        else:
            if p:
                p = table[p-1]
            else:
                r += 1

    return index

T = input()
P = input()

table = [0] * len(P)
kmp_table(P,table)
idx = kmp(P,table,T)
print(len(idx))
print(*idx)