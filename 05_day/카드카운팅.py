'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''
T = int(input())

for tc in range(T):
    result = []
    data = input()
    T = {
        'S':0, 'D':0, 'H':0, 'C':0
    }
    for i in range(0,len(data),3):
        result.append(data[i:i+3])

    result = list(set(result))
    if len(result) != (len(data)//3):
        print("#{} ERROR".format(tc+1))
        continue
    else:
        for j in range(len(result)):
            T[result[j][0]] += 1
    print("#{} ".format(tc+1), end = "")
    print(13 - T['S'], end=" ")
    print(13 - T['D'], end=" ")
    print(13 - T['H'], end=" ")
    print(13 - T['C'], end=" ")
    print()