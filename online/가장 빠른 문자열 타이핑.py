T = int(input())

for tc in range(1,T+1):
    A, B = map(str, input().split())
    i = 0
    cnt = 0
    while i <= len(A)-len(B):
        if A[i:i+len(B)] == B:
           cnt += 1
           i += len(B)
        else:
            cnt += 1
            i += 1
        if i > len(A) - len(B):
            cnt += (len(A) - i)
    print("#{} {}".format(tc, cnt))