def bfs(n,k):
    cnt = 0
    visited = [0] * 200002
    if n == k:
        print(cnt)
        print(n)
    else:
        que = []
        result = [n]
        visited[n] = 1
        que.append((result,cnt))
        while que:
            result, cnt = que.pop(0)
            n = result[-1]
            if n == k:
                print(cnt)
                print(*result)
                return
            elif n > k:
                if visited[n-1] == 0:
                    visited[n-1] = 1
                    result.append(n-1)
                    que.append((result,cnt+1))
            else:
                if n*2 < 200000:
                    if visited[n*2] == 0:
                        visited[n*2] = 1
                        que.append((result + [n*2], cnt + 1))
                if visited[n+1] == 0:
                    visited[n+1] = 1
                    que.append((result + [n+1], cnt + 1))
                if n-1 >= 0:
                    if visited[n-1] == 0:
                        visited[n-1] = 1
                        que.append((result + [n-1], cnt + 1))

N, K = map(int,input().split())
mn = 987654321
bfs(N,K)