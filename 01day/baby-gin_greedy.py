num = 112233
c = [0]*12
for i in range(6):
    c[num % 10] += 1
    num //= 10
print(c)

j = 0
run = tri = 0

while j < 10:
    if c[j] >= 3:
        c[j] -= 3
        tri += 1
        continue
    if c[j] >= 1 and c[j+1] >= 1 and c[j+2] >= 1:
        c[j] -=1
        c[j+1] -= 1
        c[j+2] -= 1
        run += 1
        continue
    j += 1
if run + tri == 2 :
    print("Baby Gin")
else:
    print("Lose")