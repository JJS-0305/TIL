def max_type(n,r):
    global mx
    # 예비 사탕 제공 후 사탕 종류 체크
    if n == r:
        cnt = 0
        for i in range(N):
            cnt += len(set(children[i][1:]))    # 종류의 개수를 체크하기 위해 set 사용
        if cnt > mx:
            mx = cnt
        return
    else:
        for candy in candys:
            # 예비 사탕을 제공했으면 다음 사탕번호로 넘어감
            if candy_chk[candy] == 1:
                continue
            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    children[i].append(candy)
                    candy_chk[candy] = 1
                    max_type(n, r+1)
                    # 재귀 호출 후 기존 상태로 초기화
                    candy_chk[candy] = 0
                    children[i].pop()
                    visited[i] = 0


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    children = [list(map(int, input().split())) for _ in range(N)]
    candys = list(range(1,M+1)) # 예비 사탕
    candy_chk = [0] * (M+1) # 예비 사탕 제공 후 체크

    # 사탕 종류가 어린이보다 적은지 여부 체크
    # 예비 사탕을 제공받은 아이 체크
    if N > M:
        visited = [0] * M
    else:
        visited = [0] * N

    mx = 0  # 사탕 종류 최대 값 반환할 변수 초기화
    max_type(len(visited),0)
    print("#{} {}".format(tc,mx))