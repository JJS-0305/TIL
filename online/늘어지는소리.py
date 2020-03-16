T = int(input())

for tc in range(1,T+1):
    string = list(input())
    H = int(input())
    loc = list(map(int, input().split()))
    cnt = [0] * (len(string)+1)
    for i in loc:
        cnt[i] += 1

    ans = ''

    for i in range(len(string)):
        for _ in range(cnt[i]):
            ans += '-'
        ans += string[i]
    for _ in range(cnt[len(string)]):
        ans += '-'
    print("#{} {}".format(tc,ans))