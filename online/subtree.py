from collections import deque
import sys

sys.stdin = open("subtree_input.txt")

def post_order(N):
    if child1[N] == 0:
        l = 0
    else: l = post_order(child1[N])
    if child2[N] == 0:
        r = 0
    else: r = post_order(child2[N])
    return l+r+1

T = int(input())

for tc in range(1,T+1):
    E, N = map(int, input().split())
    child1 = [0] * (E+2)
    child2 = [0] * (E+2)
    array = list(map(int, input().split()))
    for i in range(E):
        if child1[array[2*i]] == 0:
            child1[array[2*i]] = array[2*i+1]
        else: child2[array[2*i]] = array[2*i+1]

    ans = post_order(N)
    print("#{} {}".format(tc,ans))