T = int(input())

for tc in range(1, T+1):
    chk = input()

    for i in range(len(chk)//2):
        if chk[i] == '?' or chk[-i-1] == '?':
            continue
        elif chk[i] != chk[-i-1]:
            print("#{} Not exist".format(tc))
            break
    else:
        print("#{} Exist".format(tc))