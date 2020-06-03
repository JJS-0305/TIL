import sys
sys.stdin = open('최소신장트리_input.txt')

def make_set(v):
    p[v] = v
    rank[v] = 0

def find_set(v):
    if v == p[v]:
        return p[v]
    return find_set(p[v])

def union(v, u):
    root1 = find_set(v)
    root2 = find_set(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            p[root2] = root1
        else:
            p[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(edges):
    for v in range(V+1):
        make_set(v)

    mst = []

    edges.sort(key=lambda x:x[2])

    for edge in edges:
        n1, n2, w = edge

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            mst.append(edge)

    return mst

T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = [0] * (V+1)
    rank = [0] * (V+1)

    mst = kruskal(edges)
    tot = 0
    for i in range(len(mst)):
       tot += mst[i][2]

    print("#{} {}".format(tc, tot))