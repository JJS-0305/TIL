from collections import deque

def is_valid():
    cnt = 0 # 게임의 입력 수 체크 (반환값)
    while queue:
        r, c, n = queue.popleft()
        # 받아온 숫자 행,열번호에 맞춰 입력
        maplist[r][c] = n
        # 중복된 번호 체크를 위한 visited 리스트 생성
        visited = [0] * 10
        # 입력한 위치의 행(r) 검증
        for col in range(9):
            if maplist[r][col] == 0:
                continue
            if visited[maplist[r][col]] != 0:
                return cnt
            visited[maplist[r][col]] += 1

        # 중복된 번호 체크를 위한 visited2 리스트 생성
        visited2 = [0] * 10
        # 입력한 위치의 열(c) 검증증
        for row in range(9):
            if maplist[row][c] == 0:
                continue
            if visited2[maplist[row][c]] != 0:
                return cnt
            visited2[maplist[row][c]] += 1

        i,j = 0,0   # 입력된 위치의 3X3 격자 확인

        # 3X3위치의 행 시작점 찾기
        if r >= 0 and r < 3:
            i = 0
        elif r >= 3 and r < 6:
            i = 3
        else:
            i = 6

        # 3X3위치의 열 시작점 찾기
        if c >= 0 and c < 3:
            j = 0
        elif c >= 3 and c < 6:
            j = 3
        else:
            j = 6

        # 중복된 번호 체크를 위한 visited3 리스트 생성
        visited3 = [0] * 10
        # 입력한 위치의 3x3 격자 검증
        for row2 in range(3):
            for col2 in range(3):
                if maplist[i+row2][j+col2] == 0:
                    continue
                if visited3[maplist[i+row2][j+col2]] != 0:
                    return cnt
                visited3[maplist[i+row2][j+col2]] += 1

        cnt += 1

    return cnt

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maplist = [list(map(int,input().split())) for _ in range(9)]
    queue = deque()
    for _ in range(N):
        row, col, num = map(int, input().split())
        queue.append((row,col,num))

    ans = is_valid()
    print("#{} {}".format(tc,ans))
