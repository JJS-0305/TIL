def printlist(data, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(data[i], end =" ")
    print()

data = [1, 2, 3, 4]
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 printlist(data, bit)

n = len(data)

for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(data[j], end =" ")
    print()