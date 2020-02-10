def my_strrev(ary):
    lary = list(ary)
    for i in range(len(lary)//2):
        lary[i], lary[len(lary)-i-1] = lary[len(lary)-i-1], lary[i]
    return  ''.join(lary)

ary = "algorithm"
ary = my_strrev(ary)
print(ary)

s = "Reverse this strings"
s = s[::-1]
print(s)