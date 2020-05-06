import sys
sys.stdin = open("노드의합_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    Node = [0] * (N+1)
    for i in range(M):
        idx, val = map(int,input().split())
        Node[idx] = val

    for j in range(N,0,-1):
        if Node[j] != 0:
            continue
        elif j*2 + 1 > N:
            Node[j] = Node[j*2]
        else:
            Node[j] = Node[j * 2] + Node[j * 2 + 1]

    print("#{} {}".format(tc,Node[L]))