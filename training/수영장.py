T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    for i in range(len(plan)):
        if plan[i] > mon/day:
            plan[i] = mon/day

    for j in range(1,len(plan)):
        plan[j] = plan[j-1] + plan[j]
        if j == 2 and plan[j] > mon3/day:
            plan[j] = mon3/day
        if j >= 3:
            if plan[j] > mon3/day + plan[j-3]:
                plan[j] = mon3/day + plan[j-3]
        if j == 11:
            if plan[j] > year/day:
                plan[j] = year/day
    print("#{} {}".format(tc,int(plan[-1]*day)))