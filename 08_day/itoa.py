def itoa(s):
    ls = []
    while s > 0 :
        ls.append(chr(s%10 + ord('0')))
        s //= 10

    ls.reverse()
    return ''.join(ls)

x = 123
print(x,type(x))
str1 = itoa(x)
print(str1, type(str1))