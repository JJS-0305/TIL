#상자 회전문제

#1. 방의 크기 100일 때
def build_data(data):
    build_dt = [0] * 100
    for i in range(len(data)):
        if data[i] > 0 :
            build_dt[i] = data[i]

    return build_dt

data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
data = build_data(data)
result = [0]*100


for i in range(100):
    height = 0
    for j in range(i+1,100):
        if data[i] > data[j]:
            height += 1
        else:
            result[i] = height + 1
            break
    else:
        result[i] = 99-i
print(result)
print(max(result))

#2. 방의 크기가 data 크기일 때
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = [0]*len(data)

for i in range(len(data)):
    height = 0
    for j in range(i+1,len(data)):
        if data[i] > data[j]:
            height += 1
        else:
            result[i] = height + 1
            break
    else:
        result[i] = len(data)-i
print(result)
print(max(result))

