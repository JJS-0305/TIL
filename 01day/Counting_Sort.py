def Counting_Sort(a,b,k):
    # a[1..n] -> 입력리스트 사용된 숫자 (1~k)
    # b[1..n] -> 정렬된 리스트
    # c[1..n] -> 카운트 리스트
    c = [0] * k
    for i in range(0, len(b)):
        c[a[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1

def Counting_Sort2(a):
    b = []
    c = [0] * (max(a)+1)
    for i in range(len(a)):
        c[a[i]] += 1
    # print(c)
    for i in range(len(c)):
        if c[i] == 0:
            continue
        else:
            for _ in range(c[i]):
                b.append(i)

    return b

a = [0,4,1,3,1,2,4,1]
b = [0]* len(a)
Counting_Sort(a,b,5)
print(b)

test = Counting_Sort2(a)
print(test)