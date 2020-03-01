# def ls(row,col):
#     global star
#     for i in range(row,row+3):
#         for j in range(col,col+3):
#             if i == row + 1 and j == col + 1:
#                 continue
#             else:
#                 star[i][j] = 1
#
def print_star(n,row,col):
    for i in range(row,row+n):
        for j in range(col,col+n):
            if n == 3:
                if i == row + 1 and j == col + 1:
                    star[i][j] = 0
            if n > 3:
                if (row + n // 3 <= i < row + n//3 * 2) and (col + n//3 <= j < col + n // 3 * 2):
                    star[i][j] = 0


N = int(input())
star = [[1 for _ in range(N)] for _ in range(N)]

n = N
while n % 3 == 0 :
    for i in range(0,N,n):
        for j in range(0,N,n):
            print_star(n,i,j)
    n = n//3

for i in range(N):
    for j in range(N):
        if star[i][j] == 1:
            print('*',end="")
        else:
            print(' ',end="")
    print()