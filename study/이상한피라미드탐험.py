def level_chk(num):
    global level

    val = level[num-1] + num
    level.append(val)

    if val >= a and val >= b:
        return
    level_chk(num + 1)


T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    level = [0]
    level_chk(1)

    st = 0
    ed = 0
    for i in range(1,len(level)):
        if level[i-1] < a <= level[i]:
            st = i
            break
    for j in range(len(level),0,-1):
        if level[j - 1] < b <= level[j]:
            ed = j
            break

    d = level[st] - a - (level[ed] - b)
    gap = ed-st

    if gap < 0:
        if d < 0:
            my_min = -d - gap
        elif d > 0 and d > -gap:
            my_min = d
        else: my_min = -gap
    else:
        if d > 0:
            my_min = d + gap
        elif d < 0 and -d > gap:
            my_min = -d
        else:
            my_min = gap

    print("#{} {}".format(tc,my_min))