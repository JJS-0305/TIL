def iswall(row,col):
    if row < 0 or row >= 4:
        return False
    if col < 0 or col >= 4:
        return False
    return True

def dfs(row,col,string):
    global result
    string += maplist[row][col]
    # print(string)
    if len(string) == 7:
        result.append(string)
        return
    for i in range(4):
        test_r = row + drow[i]
        test_c = col + dcol[i]

        if iswall(test_r,test_c):
            dfs(test_r,test_c,string)

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    maplist = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for r in range(4):
        for c in range(4):
            dfs(r,c,'')
    result = list(set(result))
    print("#{} {}".format(tc,len(result)))