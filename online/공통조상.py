L, R, P = 0, 1, 2
def sizeof(node):
    result = 1
    if tree[node][L]:
        result += sizeof(tree[node][L])
    if tree[node][R]:
        result += sizeof(tree[node][R])
    return result


T = int(input())

for tc in range(1, T + 1):
    V, E, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0,0,0] for _ in range(V+1)]
    check = False

    for i in range(E):
        if tree[edges[2*i]][L] == 0:
            tree[edges[2*i]][L] = edges[2*i+1]
        else:
            tree[edges[2*i]][R] = edges[2*i+1]
        tree[edges[2*i+1]][P] = edges[2*i]

    p1 = tree[node1][P]
    pset = set()
    while p1:
        if p1 == tree[node2][P]:
            check = True
            common = p1
            break
        pset.add(p1)
        p1 = tree[p1][P]

    if check == False:
        p2 = tree[node2][P]
        while p2:
            if p2 in pset:
                common = p2
                break
            p2 = tree[p2][P]
    print("#{} {} {}".format(tc,common,sizeof(common)))
