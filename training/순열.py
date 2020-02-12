from itertools import permutations
N = int(input())
num_lst = list(map(int, input().split()))
lst = list(range(1,N+1))
a = 0
for i in permutations(lst):
    if list(i) == num_lst:
        break
    a += 1
if a == 0:
    print(-1)
else:
    b = 0
    for i in permutations(lst):
        if b == a-1:
            print(*i, sep=" ")
            break
        b += 1