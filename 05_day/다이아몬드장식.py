T = int(input())
for tc in range(T):
    char = input()
    a = '.'
    b = '.'
    c = '#'
    # print(c.format(char[0]))
    for i in char:
        a += '.#..'
        b += '#.#.'
        c += '.{}.#'.format(i)
    print(a)
    print(b)
    print(c)
    print(b)
    print(a)